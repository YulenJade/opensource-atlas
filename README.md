# 🌌 OpenSource Atlas · 开源星图

**中文** | [English](#english)

一个覆盖各领域的开源项目导航网站。每个分类展示按 GitHub Stars 排序的前 50 个匹配仓库，支持中英双语、搜索、分类和排序。

A bilingual, serverless directory of the **top 50 GitHub repositories by stars per category**.

[![Rankings](https://img.shields.io/badge/Rankings-Top%2050%20per%20category-2563eb)](#分类--categories) [![Refresh](https://img.shields.io/badge/Refresh-Daily-16a34a)](.github/workflows/update.yml) [![Pages](https://img.shields.io/badge/Hosting-GitHub%20Pages-7c3aed)](docs/index.html)

## 分类 / Categories

- **AI 与机器学习 / AI & Machine Learning** — `topic:machine-learning`
- **大语言模型 / Large Language Models** — `topic:large-language-models`
- **开发工具 / Developer Tools** — `topic:developer-tools`
- **Web 开发 / Web Development** — `topic:web-development`
- **Android 应用 / Android Apps** — `topic:android`
- **桌面软件 / Desktop Software** — `topic:desktop-app`
- **运维与云原生 / DevOps & Cloud** — `topic:devops`
- **网络安全 / Cybersecurity** — `topic:cybersecurity`
- **自动化 / Automation** — `topic:automation`
- **数据科学 / Data Science** — `topic:data-science`
- **量化与交易 / Quant & Trading** — `topic:algorithmic-trading`
- **设计与创作 / Design & Creative** — `topic:design-tools`
- **教育与学习 / Education** — `topic:education`
- **游戏开发 / Game Development** — `topic:game-development`
- **自托管软件 / Self-Hosted** — `topic:self-hosted`

## 使用与部署

1. 打开 **Actions → Refresh top 50 by category → Run workflow**，首次抓取排行榜。
2. 打开 **Settings → Pages → Build and deployment**，选择 **Deploy from a branch**、`main`、`/docs`。
3. 网站地址：**https://yulenjade.github.io/opensource-atlas/**。
4. 如果自动更新无法推送，在 **Settings → Actions → General → Workflow permissions** 中允许工作流写入仓库。

**排名说明：** 依据 `categories.json` 定义的 GitHub Search 查询，按 Stars 降序选前 50，排除 Fork 与已归档仓库。分类搜索并不等于全 GitHub 某行业的绝对排名；一个仓库可以出现在多个分类中。Stars 不代表安全或代码质量。

**版权与安全：** 仅收录公开项目元数据和链接，不复制其他仓库的源码，不保证项目安全、可用或盈利。

## English

OpenSource Atlas is a bilingual directory for discovering GitHub repositories across 15 categories. Each category lists the top 50 repositories matching a defined GitHub Search query, ordered by stars, excluding forks and archived repositories.

**Deploy:** Manually run the **Refresh top 50 by category** workflow in GitHub Actions; then configure GitHub Pages to publish the `/docs` folder from `main`. Daily refreshes use the repository's built-in `GITHUB_TOKEN`.

**Limitations:** These are query-specific rankings, not an authoritative global ranking of every field. A repository may appear in multiple categories. Stars are not a security or quality endorsement.

To add a category, edit `categories.json` and rerun the workflow.
