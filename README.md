# Daojia · 道家与道教传统顾问

一个面向 ChatGPT、Codex 与兼容 Skills 环境的开源 AI Skill，提供可溯源的道家哲学、道教文献、教派、神仙谱系、科仪、符箓、内丹、风水、八字、紫微与传统术数分析。

> Source-grounded Daoist studies and traditional-model guidance for AI assistants.

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Catalog](https://img.shields.io/badge/Daorenjia%20Catalog-1%2C524%20works-8b0000.svg)](skill/references/daorenjia-catalog.tsv)

## 项目特点

- **来源可追溯**：区分原典、注本、宗教传统、地方民俗、现代观点和网络传言。
- **流派不混用**：回答前明确正一、全真及具体术数体系，保留不同流派的规则差异。
- **经书目录内置**：收录“道人家”24 个细分类目的 1,524 部文献索引，其中 591 部匹配网站的“已校对”目录。
- **按需检索**：内置经名、部类、原页链接和校对状态，不把数千万字正文强塞进每次对话。
- **拒绝凭空排盘**：八字、紫微、节气、历法等必须使用确定性计算工具；没有可靠计算器时不伪造结果。
- **创作友好**：适合小说、AI 短剧和游戏设定，可将内容分为“文献依据、合成还原、艺术虚构”。
- **安全边界**：不冒充道士、法师或授箓人员，不保证超自然效果，不使用恐吓营销。

## 能力范围

| 领域 | 支持内容 |
| --- | --- |
| 道家与经书 | 《道德经》《庄子》及道教经典的出处、释义、版本与注家比较 |
| 道教历史 | 教派、制度、人物、神仙谱系、法脉与历史语境 |
| 科仪与术法 | 符箓、斋醮、科仪、雷法、咒诀、章表等公开文献层面的考据 |
| 内丹与修持 | 术语、理论、历史传统及风险边界 |
| 风水 | 形势、理气及不同体系的传统模型分析 |
| 命理术数 | 八字、紫微、择日、奇门、六壬、太乙等的规则化分析 |
| 内容创作 | 为小说、短剧、漫画和游戏提供可标注真实性层级的素材 |

## 安装

下载或克隆本仓库，将 [`skill/`](skill/) 目录作为一个完整 Skill 导入兼容的 ChatGPT/Codex Skills 环境。

```bash
git clone https://github.com/weeduon/daojia.git
```

安装时应以 `skill/SKILL.md` 为 Skill 主文件，并保留同级的 `agents/`、`references/` 和 `scripts/`。

## 使用示例

```text
使用 $daoist-advisor，比较《太上老君说常清静妙经》不同注本的解释。
```

```text
使用 $daoist-advisor，核实这段咒语是否有道藏出处，并区分文献事实和网络说法。
```

```text
使用 $daoist-advisor，把正一科仪改编成 AI 短剧，并标注真实考据与艺术虚构。
```

```text
使用 $daoist-advisor，告诉我排八字还缺少哪些资料，不要猜测出生时间。
```

## “道人家”文献索引

项目内置 [`daorenjia-catalog.tsv`](skill/references/daorenjia-catalog.tsv)，作为文献定位索引：

- 24 个细分类目；
- 1,524 条唯一文献记录；
- 591 条匹配网站自身的“已校对”索引；
- 保存部类、经名、原页链接和网站校对状态；
- 不保存第三方经文全文。

本地检索：

```bash
rg -n -F '太上老君说常清静妙经' skill/references/daorenjia-catalog.tsv
```

刷新索引：

```bash
python3 skill/scripts/build_daorenjia_catalog.py
```

抓取器只访问栏目列表和网站的“已校对”索引，并设置限速；它不会下载经书正文。

## 目录结构

```text
.
├── README.md
├── LICENSE
├── NOTICE
└── skill/
    ├── SKILL.md
    ├── agents/
    │   └── openai.yaml
    ├── references/
    │   ├── daorenjia-catalog.tsv
    │   ├── daorenjia-source-guide.md
    │   ├── domain-routing.md
    │   ├── metaphysics.md
    │   ├── ritual-safety.md
    │   └── source-policy.md
    └── scripts/
        └── build_daorenjia_catalog.py
```

## 资料、版权与引用

本项目的代码、Skill 指令和原创说明采用 [Apache License 2.0](LICENSE)。

`daorenjia-catalog.tsv` 是元数据索引，不是经书正文镜像。“道人家”网站说明其文本来自多个网络来源，并由维护者对照《中华道藏》DJVU 影像逐步校对；网站未显示明确的开放内容许可证。因此：

- 本仓库不复制该网站的完整经文、现代题解、图片或数据库正文；
- 第三方经文整理、标点、题解、影像及网页内容的权利归各自权利人；
- 网站“已校对”表示站方自述的校对状态，不等同于学术定本；
- 引用具体经文时应访问原页面、核对图片版，并尽可能与独立版本交叉验证。

来源说明：[道人家·关于本站](https://www.daorenjia.com/about.php)

## 安全声明

本项目用于传统文化、文献研究和创作辅助：

- 不代表任何道教组织、宫观、法脉或宗教教职人员；
- 不授予皈依、冠巾、传度、传戒、授箓或主持法事资格；
- 风水、命理和占卜仅作为传统文化模型，不是科学确定性预测；
- 不应替代医疗、心理、法律、投资、建筑安全等专业意见；
- 不提供伤害、胁迫、诈骗、危险服食或伪造宗教身份的方法。

## 贡献

欢迎提交问题和改进建议。新增资料时请：

1. 写明书名、篇章、版本、页码或稳定链接；
2. 区分原文、转述、传统解释与个人推论；
3. 不提交未经授权的现代著作、数据库或网站全文；
4. 不把小说、短视频或匿名秘法伪称为道藏原文；
5. 对不同流派保留明确标签，不强行合并。

## License

Apache License 2.0。第三方链接、书目元数据及外部来源内容不因本项目许可证而改变其原有权利状态，详见 [NOTICE](NOTICE)。
