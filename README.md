# 🌌 OpenSource Atlas · 开源星图

**中文** | [English](#english)

**V2.0 已上线：** 高级搜索（语言、许可证、最近活跃）、11 大领域侧边导航、移动端适配、2～4 项目对比、本地收藏和 JSON 导出、深浅色主题，以及采集失败时的缓存保留。无需账号或独立服务器。\n\n一个覆盖各领域的开源项目导航网站。每个分类展示按 GitHub Stars 排序的前 50 个匹配仓库，支持中英双语、搜索、分类和排序。

A bilingual, serverless directory of the **top 50 GitHub repositories by stars per category**.

[![Rankings](https://img.shields.io/badge/Rankings-Top%2050%20per%20category-2563eb)](#分类--categories) [![Refresh](https://img.shields.io/badge/Refresh-Daily-16a34a)](.github/workflows/update.yml) [![Pages](https://img.shields.io/badge/Hosting-GitHub%20Pages-7c3aed)](docs/index.html)

## 分类 / Categories

**11 个一级领域 / 63 个细分类 / 每类 Top 50**。

| 一级领域 | Category group |
|---|---|
| 人工智能 | Artificial Intelligence |
| 编程与开发 | Development |
| 操作系统与应用 | Operating Systems & Apps |
| 服务器与基础设施 | Infrastructure |
| 安全与隐私 | Security & Privacy |
| 自动化与机器人 | Automation & Bots |
| 数据与数据库 | Data & Databases |
| 金融与区块链 | Finance & Blockchain |
| 设计与多媒体 | Design & Media |
| 教育与科学 | Education & Science |
| 游戏与娱乐 | Games & Entertainment |

完整细分类及 GitHub 搜索规则：[categories.json](categories.json)。

## V2.0 功能 / Features\n\n- **高级筛选 / Advanced filters:** 语言、许可证、近 30/90 天活跃、Stars 和最近提交排序。\n- **比较 / Compare:** 最多比较四个项目的 Stars、语言、许可证和最近提交。\n- **收藏 / Favorites:** 保存在当前浏览器 localStorage，支持 JSON 导出；不会跨设备同步。\n- **移动端 / Mobile:** 响应式导航与中英双语界面、深浅色主题。\n- **可靠更新 / Resilient refresh:** API 请求重试，失败分类使用已有缓存；全部失败则保留原始数据并让工作流失败。\n\n## 使用与部署

1. 打开 **Actions → Refresh top 50 by category → Run workflow**，首次抓取排行榜。
2. 打开 **Settings → Pages → Build and deployment**，选择 **Deploy from a branch**、`main`、`/docs`。
3. 网站地址：**https://yulenjade.github.io/opensource-atlas/**。
4. 如果自动更新无法推送，在 **Settings → Actions → General → Workflow permissions** 中允许工作流写入仓库。

**排名说明：** 依据 `categories.json` 定义的 GitHub Search 查询，按 Stars 降序选前 50，排除 Fork 与已归档仓库。分类搜索并不等于全 GitHub 某行业的绝对排名；一个仓库可以出现在多个分类中。Stars 不代表安全或代码质量。

**版权与安全：** 仅收录公开项目元数据和链接，不复制其他仓库的源码，不保证项目安全、可用或盈利。

## English

OpenSource Atlas is a bilingual directory for discovering GitHub repositories across 63 categories across 11 groups. Each category lists the top 50 repositories matching a defined GitHub Search query, ordered by stars, excluding forks and archived repositories.

**Deploy:** Manually run the **Refresh top 50 by category** workflow in GitHub Actions; then configure GitHub Pages to publish the `/docs` folder from `main`. Daily refreshes use the repository's built-in `GITHUB_TOKEN`.

**Limitations:** These are query-specific rankings, not an authoritative global ranking of every field. A repository may appear in multiple categories. Stars are not a security or quality endorsement.

To add a category, edit `categories.json` and rerun the workflow.
