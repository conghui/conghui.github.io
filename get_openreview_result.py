import openreview
import time
from collections import Counter
from difflib import SequenceMatcher

try:
    import arxiv

    HAS_ARXIV = True
except ImportError:
    HAS_ARXIV = False


def _normalize_title(title):
    """标准化标题用于相似度比较：小写、去标点、合并空格"""
    if not title:
        return ""
    s = title.lower().strip()
    for c in ".,;:!?\"'()[]{}":
        s = s.replace(c, " ")
    return " ".join(s.split())


def _find_arxiv_link(title, similarity_threshold=0.80):
    """
    根据论文标题在 arXiv 检索，返回匹配的 arXiv 链接。
    若标题相同或非常接近则认为是同一篇论文。
    """
    if not HAS_ARXIV or not title or len(title) < 10:
        return None
    try:
        query_title = title[:200] if len(title) > 200 else title
        client = arxiv.Client()
        search = arxiv.Search(query=f"ti:{query_title}", max_results=10)
        best_match = None
        best_ratio = 0.0
        norm_our = _normalize_title(title)
        for result in client.results(search):
            norm_arxiv = _normalize_title(result.title)
            ratio = SequenceMatcher(None, norm_our, norm_arxiv).ratio()
            if ratio > best_ratio:
                best_ratio = ratio
                best_match = result
        if best_match and best_ratio >= similarity_threshold:
            # 提取 arXiv ID
            arxiv_id = best_match.entry_id.split("/")[-1]
            return arxiv_id
    except Exception:
        pass
    return None


VENUE_MAPPING = {
    "NIPS": "NeurIPS",
    "NeurIPS": "NeurIPS",
    "ICLR": "ICLR",
    "CVPR": "CVPR",
    "ICCV": "ICCV",
    "ACL": "ACL",
    "EMNLP": "EMNLP",
    "NAACL": "NAACL",
    "ECCV": "ECCV",
    "ICML": "ICML",
    "AAAI": "AAAI",
    "IJCAI": "IJCAI",
}


def normalize_venue(venue):
    """
    标准化会议名称

    :param venue: 原始会议名称
    :return: 标准化后的会议名称
    """
    venue = venue.strip()

    # 提取年份（查找第一个数字）
    year = ""
    for word in venue.split():
        if word.isdigit() and len(word) == 4:
            year = word
            break

    # 标准化会议名称
    for key, value in VENUE_MAPPING.items():
        if key in venue:
            return f"{value} {year}".strip()

    # 如果没有匹配到，返回原始名称
    return venue


def generate_paper_links(papers):
    """
    生成论文链接列表

    :param papers: 论文列表 [(title, authors, venue, link, decision), ...]
    :return: Markdown 链接列表
    """
    links = []
    for i, (title, authors, venue, link, decision) in enumerate(papers, 1):
        # 使用 OpenReview 链接
        paper_link = f"https://openreview.net/pdf?id={link.split('=')[-1]}"
        links.append(f"[{i}]({paper_link})")
    return links


def check_and_update_news(accepted_papers, about_md_path):
    """
    检查 about.md 的 news 部分，如果会议中稿未添加则更新

    :param accepted_papers: 中稿论文列表 [(title, authors, venue, link, decision), ...]
    :param about_md_path: about.md 文件路径
    """
    try:
        # 1. 读取 about.md
        with open(about_md_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        # 2. 找到 news 区域
        news_start_idx = None
        news_end_idx = None
        for i, line in enumerate(lines):
            if line.strip() == "# 🔥 Recent News":
                news_start_idx = i
            elif line.strip() == "# 💻 Open-source Projects":
                news_end_idx = i
                break

        if news_start_idx is None or news_end_idx is None:
            print("[错误] 未找到 news 区域")
            return

        # 3. 解析现有 news
        existing_news = []
        for i in range(news_start_idx + 1, news_end_idx):
            line = lines[i].strip()
            if line.startswith("- *") and "*:" in line:
                # 解析时间戳 - 提取 YYYY.MM 部分 (去掉星号)
                timestamp = line[2 : line.index("*:", 2)]  # 得到 "*2025.12"
                timestamp = timestamp.strip("*")  # 去掉星号得到 "2025.12"
                existing_news.append((timestamp, line))

        # 4. 检查中稿论文是否已添加
        if not accepted_papers:
            print("[信息] 没有中稿论文需要处理")
            return

        # 获取会议信息
        first_paper = accepted_papers[0]
        venue = normalize_venue(first_paper[2])
        # 从标准化的 venue 中提取年份
        year = ""
        for word in venue.split():
            if word.isdigit() and len(word) == 4:
                year = word
                break

        # 检查是否已存在
        existing_found = False
        venue_name = venue.split()[0]  # e.g., "ICLR"
        for timestamp, news_line in existing_news:
            # 同时匹配会议名称和年份，确保不误匹配 ICLR 2025 和 ICLR 2026
            if (
                venue_name in news_line
                and year in news_line
                and f"{venue_name} {year}" in news_line
            ):
                existing_found = True
                break

        if existing_found:
            print(f"[信息] 会议 {venue} 已在 news 中存在，无需更新")
            return

        # 5. 生成新条目
        timestamp, news_content = generate_news_entry(accepted_papers)

        # 6. 找到插入位置（按时间倒序插入到正确位置）
        insert_pos = news_start_idx + 1
        for i, (existing_timestamp, _) in enumerate(existing_news):
            if compare_timestamps(timestamp, existing_timestamp) > 0:
                insert_pos = news_start_idx + 1 + i
                break

        # 7. 插入新条目
        new_entry = f"- *{timestamp}*: 🎉 {news_content}\n"
        lines.insert(insert_pos, new_entry)

        # 8. 保存文件
        with open(about_md_path, "w", encoding="utf-8") as f:
            f.writelines(lines)

        print(f"[成功] 已更新 about.md，添加了 {len(accepted_papers)} 篇中稿论文")

    except Exception as e:
        print(f"[错误] 更新 about.md 失败: {e}")


def compare_timestamps(ts1, ts2):
    """
    比较两个时间戳，返回正数表示 ts1 更新

    :param ts1: 时间戳1 (格式: YYYY.MM)
    :param ts2: 时间戳2 (格式: YYYY.MM)
    :return: 正数表示 ts1 更新，负数表示 ts2 更新
    """
    y1, m1 = map(int, ts1.split("."))
    y2, m2 = map(int, ts2.split("."))

    if y1 != y2:
        return y1 - y2
    return m1 - m2


def generate_news_entry(papers):
    """
    生成 news 条目

    :param papers: 论文列表
    :return: (timestamp, news_content)
    """
    # 获取最早的年月作为时间戳
    years = [int(p[2].split()[-1]) for p in papers if p[2].split()[-1].isdigit()]
    months = [int(p[2].split()[-2][1:3]) for p in papers if p[2].split()[-1].isdigit()]

    if not years:
        # 如果无法获取年份，使用当前年份
        from datetime import datetime

        year = datetime.now().year
        month = datetime.now().month
    else:
        year = min(years)
        month = min([m for i, m in enumerate(months) if years[i] == year])

    timestamp = f"{year}.{month:02d}"

    # 生成论文链接
    links = generate_paper_links(papers)

    # 生成内容
    if len(papers) == 1:
        content = f"{links[0]} paper is accepted by {normalize_venue(papers[0][2])}."
    else:
        content = (
            " ".join(links)
            + f" papers are accepted by {normalize_venue(papers[0][2])}."
        )

    return timestamp, content


class OpenReviewTracker:
    def __init__(self, username, password, use_v2=True):
        """
        初始化客户端。
        近年来主流顶会（ICLR 2024+, NeurIPS 2023+）均已迁移至 API v2。
        """
        baseurl = (
            "https://api2.openreview.net" if use_v2 else "https://api.openreview.net"
        )
        self.client = openreview.api.OpenReviewClient(
            baseurl=baseurl, username=username, password=password
        )
        print(f"[系统] 已连接至 OpenReview API ({baseurl})")

    def analyze_my_papers(self, profile_id):
        """
        第一性原理：你是谁？你发了什么？
        通过 authorids 过滤属于你的所有 Note，并解构其回复（审稿与决定）。

        :param profile_id: 你的 OpenReview ID (如 ~San_Zhang1) 或注册邮箱
        """
        print(f"\n--- 正在检索 [{profile_id}] 的论文状态 ---")

        # 获取作为作者的所有论文，同时带上所有关联的回复（包含Review和Decision）
        # 避免 N+1 查询问题，一次性拉取。
        my_submissions = self.client.get_all_notes(
            content={"authorids": profile_id}, details="replies"
        )

        if not my_submissions:
            print("[结果] 未找到关联的论文。")
            return

        for paper in my_submissions:
            title = paper.content.get("title", {}).get("value", "未知标题")
            venue = paper.content.get("venue", {}).get("value", "正在审稿/未知会议")
            print(f"\n➤ 论文: {title}")
            print(f"  会议状态: {venue}")
            print(f"  链接: https://openreview.net/forum?id={paper.forum}")

            replies = paper.details.get("replies", [])
            reviews = []
            decision = "尚未出结果"

            for reply in replies:
                invitations = reply.get("invitations", [])

                # 提取审稿意见
                if any("Review" in inv for inv in invitations):
                    # 不同会议的 rating 字段可能不同 (如 'rating', 'recommendation')
                    rating_val = reply["content"].get("rating", {}).get("value")
                    confidence_val = reply["content"].get("confidence", {}).get("value")
                    if rating_val is not None:
                        rating_str = (
                            str(rating_val).split(":")[0]
                            if isinstance(rating_val, str)
                            else str(rating_val)
                        )
                        reviews.append(f"分数: {rating_str} | 置信度: {confidence_val}")

                # 提取最终决定
                if any("Decision" in inv for inv in invitations):
                    decision = (
                        reply["content"].get("decision", {}).get("value", "未知决定")
                    )

            # 输出结构化信息
            print("  [审稿意见]:")
            if reviews:
                for r in reviews:
                    print(f"    - {r}")
            else:
                print("    - 暂无审稿意见")

            print(f"  [最终决定]: {decision}")

    def analyze_conference_stats(self, venue_id):
        """
        出题人视角：看清宏观基本面。
        获取会议所有提交，统计存活率与录用分布。

        :param venue_id: 会议 ID，例如 'ICLR.cc/2024/Conference'
        """
        print(f"\n--- 正在分析会议大盘: {venue_id} ---")
        invitation_id = f"{venue_id}/-/Submission"

        try:
            # 获取所有该会议的提交记录
            submissions = self.client.get_all_notes(invitation=invitation_id)
            total_submissions = len(submissions)
            print(f"[数据] 共拉取到 {total_submissions} 篇有效提交。")

            decisions_counter = Counter()

            # 遍历统计
            for paper in submissions:
                # 最终录用的论文，其 venue 字段通常会被修改为具体的 track (如 Poster, Oral)
                # 被拒的论文 venue 通常还是 Submission 或者被标记为 Reject
                venue_value = paper.content.get("venue", {}).get("value", "Unknown")

                # 粗略分类逻辑（可根据具体会议后缀微调）
                if "Reject" in venue_value:
                    decisions_counter["Reject"] += 1
                elif "Withdraw" in venue_value or "Desk Reject" in venue_value:
                    decisions_counter["Withdrawn/Desk Reject"] += 1
                elif venue_value == "Unknown" or "Submission" in venue_value:
                    decisions_counter["Pending (审稿中)"] += 1
                else:
                    # 录用状态 (e.g., ICLR 2024 Poster, Oral, Spotlight)
                    decisions_counter[f"Accept ({venue_value})"] += 1

            # 汇总计算
            print("\n[全局录用情况统计]:")
            accepted_total = sum(
                v for k, v in decisions_counter.items() if "Accept" in k
            )

            for status, count in decisions_counter.most_common():
                ratio = (count / total_submissions) * 100
                print(f"  {status}: {count} 篇 ({ratio:.1f}%)")

            if total_submissions > 0 and accepted_total > 0:
                overall_accept_rate = (accepted_total / total_submissions) * 100
                print(f"\n👉 宏观结论：当前总录用率约为 {overall_accept_rate:.1f}%")

        except openreview.OpenReviewException as e:
            print(f"[错误] 无法获取数据，请检查 venue_id 是否正确。API 返回: {e}")

    def get_my_accepted_papers_in_venues(self, profile_id, venue_patterns):
        """
        获取你在指定会议中中稿的论文列表。

        :param profile_id: 你的 OpenReview ID (如 ~Conghui_He2)
        :param venue_patterns: 会议匹配模式列表，例如 ['ICLR 2025', 'ICLR 2026', 'NeurIPS 2025']
                              只要论文的会议状态(venue)包含任一模式即视为该会议，不区分大小写
        :return: 中稿论文列表 [(title, venue, link, decision), ...]
        """
        print(f"\n--- 检索 [{profile_id}] 在指定会议中的中稿论文 ---")
        print(f"目标会议: {venue_patterns}")

        my_submissions = self.client.get_all_notes(
            content={"authorids": profile_id}, details="replies"
        )

        if not my_submissions:
            print("[结果] 未找到关联的论文。")
            return []

        accepted_in_venues = []
        patterns_lower = [p.lower() for p in venue_patterns]

        for paper in my_submissions:
            title = paper.content.get("title", {}).get("value", "未知标题")
            venue = paper.content.get("venue", {}).get("value", "正在审稿/未知会议")
            link = f"https://openreview.net/forum?id={paper.forum}"

            # 提取作者列表（兼容 content.authors.value 或 content.authors 等格式）
            authors_raw = paper.content.get("authors")
            if authors_raw is None:
                authors_str = "未知作者"
            else:
                authors_list = (
                    authors_raw.get("value", authors_raw)
                    if isinstance(authors_raw, dict)
                    else authors_raw
                )
                authors_str = (
                    ", ".join(authors_list)
                    if isinstance(authors_list, list)
                    else str(authors_list)
                )

            # 判断是否为指定会议：venue 包含任一 pattern
            venue_lower = venue.lower()
            if not any(p in venue_lower for p in patterns_lower):
                continue

            # 提取最终决定
            decision = "尚未出结果"
            replies = paper.details.get("replies", [])
            for reply in replies:
                invitations = reply.get("invitations", [])
                if any("Decision" in inv for inv in invitations):
                    decision = (
                        reply["content"].get("decision", {}).get("value", "未知决定")
                    )
                    break

            # 判断是否录用：decision 含 Accept（不含 Reject）
            if "Accept" in decision and "Reject" not in decision:
                accepted_in_venues.append((title, authors_str, venue, link, decision))

        # 输出结果
        print(f"\n[共找到 {len(accepted_in_venues)} 篇中稿论文]\n")
        for i, (title, authors_str, venue, link, decision) in enumerate(
            accepted_in_venues, 1
        ):
            print(f"{i}. {title}")
            print(f"   作者: {authors_str}")
            print(f"   会议: {venue} | 决定: {decision}")
            print(f"   链接: {link}\n")

        return accepted_in_venues


if __name__ == "__main__":
    # 配置你的账户信息 (建议通过环境变量传入，避免硬编码)
    USERNAME = "heconghui@pjlab.org.cn"
    PASSWORD = "jwc6yte7AJN4qjp!rbh"

    # 你的 OpenReview ID，例如 '~Your_Name1'
    MY_PROFILE_ID = "~Conghui_He2"

    # 你关心的会议列表（用于筛选中稿论文），与 venue 字段做包含匹配
    # 例如 venue 为 "ICLR 2025 Spotlight" 时，命中 "ICLR 2025"
    MY_TARGET_VENUES = [
        # "ICLR 2025",
        "ICLR 2026",
        # "NeurIPS 2025",
        # "ICCV 2025",
        # "CVPR 2025",
        # "CVPR 2026",
        # "ACL 2025",
        # "EMNLP 2024",
    ]

    # 会议大盘分析用（可选）
    TARGET_VENUE = "ICLR.cc/2026/Conference"

    # about.md 文件路径
    ABOUT_MD_PATH = "_pages/about.md"

    tracker = OpenReviewTracker(username=USERNAME, password=PASSWORD)

    # 1. 获取我在指定会议中的中稿论文
    accepted_papers = tracker.get_my_accepted_papers_in_venues(
        MY_PROFILE_ID, MY_TARGET_VENUES
    )

    # 2. 检查并更新 about.md 的 news 部分
    if accepted_papers:
        check_and_update_news(accepted_papers, ABOUT_MD_PATH)

    # 3. 检查个人论文微观状态（可选，注释掉可加快运行）
    # tracker.analyze_my_papers(MY_PROFILE_ID)

    # 4. 纵览会议宏观大盘（可选）
    # tracker.analyze_conference_stats(TARGET_VENUE)
