# 🎬 电影数据智能爬取与可视化分析平台

> **豆瓣 Top250 全链路数据处理流水线：爬虫 → 清洗 → 聚合 → 看板**  
> 面向大数据应用开发的工程实践项目，具备可扩展架构与大数据迁移能力。

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.25+-red)](https://streamlit.io/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0+-150458)](https://pandas.pydata.org/)

## 📖 目录

- [项目简介](#项目简介)
- [核心功能](#核心功能)
- [技术架构](#技术架构)
- [项目结构](#项目结构)
- [快速开始](#快速开始)
- [使用说明](#使用说明)
- [数据分析洞察示例](#数据分析洞察示例)
- [可扩展性设计](#可扩展性设计)
- [工程规范](#工程规范)
- [未来规划](#未来规划)
- [作者](#作者)

---

## 项目简介

独立设计并实现的一个端到端数据应用开发项目，完整覆盖**网页数据抓取 → 数据清洗 → 多维聚合分析 → 交互式可视化看板**的全流程。项目采用面向对象思想构建可扩展爬虫框架，内建请求伪装与指数退避重试机制；利用 Pandas 完成多维统计，并基于 Streamlit 搭建交互看板，支持动态筛选与图表联动。

**核心理念**：逻辑与引擎解耦、计算与存储分离、流程原子化，使得当数据量增长时可以平滑迁移至 PySpark 等大数据处理引擎。

---

## 核心功能

- ✅ **高可用爬虫框架**  
  抽象基类封装 Session 管理、User-Agent 伪装、指数退避重试，子类只需实现解析方法，新增数据源零侵入。

- ✅ **精准数据解析**  
  XPath 定位豆瓣电影条目，正则清洗票房（多币种/多单位统一为“亿”）、时长、评价人数等非结构化字段。

- ✅ **全量数据持久化**  
  爬取结果经清洗后落地为 CSV，支持后续离线分析，避免重复请求。

- ✅ **多维聚合统计**  
  按年份、国家/地区、类型进行聚合，计算电影产量趋势、年均评分、类型分布等关键指标。

- ✅ **交互式可视化看板**  
  Streamlit 搭建数据驾驶舱，支持按年份区间、最低评分动态过滤，双轴图、饼图、排行榜多视图联动。

- ✅ **开闭原则架构**  
  解析与清洗、分析与可视化各层解耦，新增 IMDB/TMDB 数据源只需新增一个子类，不改其他模块。

---

## 技术架构

数据采集层 (Crawler) ──→ 数据清洗层 (Cleaner) ──→ 数据分析层 (Analysis) ──→ 可视化层 (Visualization) ──→ 应用层 (Streamlit)
requests pandas pandas matplotlib Streamlit
lxml / XPath 正则 groupby / agg 中文支持 tabs / sidebar
指数退避重试 缺失值/单位标准化 多维透视 双轴图 / 饼图 动态筛选联动
text


**技术栈**：`Python 3.8+` · `requests` · `lxml` · `XPath` · `正则表达式` · `Pandas` · `Matplotlib` · `Streamlit` · `面向对象设计` · `异常重试机制`

---

## 项目结构

movie_insight/
├── crawler/ # 爬虫模块
│ ├── init.py
│ ├── base_crawler.py # 抽象基类：请求、重试、日志
│ └── douban_crawler.py # 豆瓣Top250具体实现
├── data/ # 数据清洗与持久化
│ ├── init.py
│ └── cleaner.py # 格式清洗、缺失值处理
├── analysis/ # 数据分析与聚合
│ ├── init.py
│ └── aggregator.py # 分年、分类型、分国家统计
├── visualization/ # 可视化图表
│ ├── init.py
│ └── plots.py # 趋势图、饼图、横向柱状图
├── output/ # 数据输出目录
│ └── movies.csv # 清洗后的结构化数据
├── app.py # Streamlit 应用入口
├── run_crawler.py # 一键运行爬虫并保存数据
├── requirements.txt # Python 依赖清单
├── config.py # 请求头、URL等配置
└── README.md # 项目说明文档

> 目录结构清晰，模块职责单一，遵循 Python 标准项目布局。

---

## 快速开始

### 环境要求
- Python 3.8 或更高版本
- pip 包管理器

### 安装步骤

1. **克隆仓库**
   ```bash
   git clone https://github.com/[你的GitHub用户名]/douban-top250-crawler-visualization.git
   cd douban-top250-crawler-visualization
2. 安装依赖
bash
pip install -r requirements.txt
3. 运行爬虫（获取最新数据）
bash
python run_crawler.py
脚本会依次爬取豆瓣 Top250 所有分页，清洗后保存到 output/movies.csv。
4. 启动交互看板
bash
streamlit run app.py
浏览器自动打开 http://localhost:8501，即可看到数据驾驶舱。

使用说明
• 爬虫配置：可在 config.py 中修改请求头、超时、重试次数、目标URL等参数。
• 新增数据源：只需在 crawler/ 下新增子类，继承 BaseCrawler，实现 parse 方法，并返回统一结构的字典列表即可。
• 看板筛选：左侧边栏可调整年份范围、最低评分，主区域四个 Tab 分别展示年度趋势、高分类型分布、国家/地区分布、票房排行。
• 中文显示：visualization/plots.py 已配置中文字体，若系统无 SimHei 字体可改为其他可用中文字体。
￼
数据分析洞察示例
基于豆瓣 Top250 数据，平台可以快速发现以下规律：
• 📈 90 年代是高分电影黄金期：1990-2000 年间上映的电影数量及平均评分均处于高位。
• 🥧 剧情类主宰高分区间：评分 ≥ 9.0 的电影中，剧情类占比超过 40%。
• 🌍 美国电影占据半壁江山：Top250 中美国电影数量断层领先，其次为日本、中国。
• 💰 票房数据稀疏：仅少部分商业片有完整票房记录，老电影及文艺片票房缺失较多。

可扩展性设计
本项目在设计上刻意遵循了大数据工程的核心原则，便于后续向生产级平台演进：

维度            当前实现           可扩展至
计算引擎        Pandas (单机)      PySpark (分布式)，算子同构，逻辑不变
数据存储        CSV                SQLite/MySQL → Hive/Delta Lake
任务调度        手动运行脚本        Airflow DAG 定时调度
数据源          豆瓣Top250         TMDB、IMDB、Box Office Mojo 等
部署方式        本地 Streamlit      Docker 容器化 → 云服务器部署
这种“逻辑与引擎分离”的设计，使得核心分析代码在数据量从 250 条增长到 TB 级时，只需切换执行环境而无需重写业务逻辑。

工程规范
本项目严格遵循以下工程习惯：
• ✅ 代码风格：所有模块均遵循 PEP8 规范，可执行 flake8 或 pylint 检查。
• ✅ 模块化设计：爬虫、清洗、分析、可视化各层独立，高内聚低耦合。
• ✅ 日志与异常：统一使用 logging 模块记录关键步骤和错误，便于追踪。
• ✅ 版本控制：使用 Git 进行源码管理，.gitignore 忽略 __pycache__、虚拟环境、输出数据等。
• ✅ 文档完整：核心函数均附 docstring，README 涵盖安装、使用、架构说明。

未来规划
• 新增 TMDB 或 IMDB 爬虫，实现多源数据融合与交叉验证
• 将数据存储升级为 SQLite，支持复杂 SQL 查询
• 编写 Dockerfile，实现一键容器化部署
• 引入 Apache Airflow，定时更新数据并发送分析报告
• 使用 PySpark 重构聚合层，验证大数据量下的性能表现

作者
马晨阁
Python 数据开发实习生求职中
📧 Email: Macheng216@outlook.com
📱 电话: 18836122072
🔗 GitHub: @macheng216 
￼
如果你觉得这个项目对你有帮助，欢迎给个 ⭐ Star ！
如有技术问题或工作机会，也欢迎直接联系我。
