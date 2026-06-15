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
独立设计并实现的端到端数据应用开发项目，完整覆盖**网页数据抓取 → 数据清洗 → 多维聚合分析 → 交互式可视化看板**全流程。
采用面向对象思想搭建可扩展爬虫框架，内置请求伪装、指数退避重试机制；借助 Pandas 完成多维统计分析，基于 Streamlit 搭建交互式数据看板，支持筛选条件动态调整、多图表联动展示。

**核心理念**：逻辑与引擎解耦、计算与存储分离、流程原子化，数据量增长后可无缝迁移至 PySpark 分布式大数据引擎。

---

## 核心功能
- ✅ **高可用爬虫框架**
  抽象基类统一封装Session会话、UA伪装、指数退避重试逻辑，子类仅需重写解析函数，新增数据源无需改动底层代码。

- ✅ **精准数据解析**
  XPath定位豆瓣电影条目，正则表达式标准化清洗票房（多币种、多单位统一换算为“亿”）、影片时长、评分人数等非结构化文本字段。

- ✅ **全量数据持久化**
  爬虫原始数据清洗后落地为CSV结构化文件，支持离线重复分析，避免重复发送网络请求触发反爬。

- ✅ **多维聚合统计**
  按照上映年份、制片国家/地区、影片类型分组聚合，计算影片产量趋势、平均分、类型占比等业务指标。

- ✅ **交互式可视化看板**
  基于Streamlit搭建数据驾驶舱，支持自定义年份区间、最低评分过滤条件，双轴趋势图、饼图、排行榜多视图联动展示。

- ✅ **低耦合可扩展架构**
  数据解析、清洗、统计、可视化分层解耦，新增IMDB/TMDB等数据源仅新增对应爬虫子类，原有业务代码无侵入修改。

---

## 技术架构
数据采集层 (Crawler) ──→ 数据清洗层 (Cleaner) ──→ 数据分析层 (Analysis) ──→ 可视化层 (Visualization) ──→ 应用层 (Streamlit)
requests pandas pandas matplotlib Streamlit
lxml / XPath 正则 groupby /agg 中文支持 tabs /sidebar
指数退避重试 缺失值 / 单位标准化 多维透视 双轴图 / 饼图 动态筛选联动
**技术栈**：`Python 3.8+` · `requests` · `lxml` · `XPath` · `正则表达式` · `Pandas` · `Matplotlib` · `Streamlit` · 面向对象设计 · 异常重试机制

---

## 项目结构
movie_insight/
├── crawler/ # 爬虫模块
│ ├── init.py
│ ├── base_crawler.py # 抽象基类：请求、重试、日志封装
│ └── douban_crawler.py # 豆瓣 Top250 爬虫具体业务实现
├── data/ # 数据清洗与持久化模块
│ ├── init.py
│ └── cleaner.py # 格式清洗、缺失值填充、单位标准化
├── analysis/ # 数据分析与聚合模块
│ ├── init.py
│ └── aggregator.py # 分年份、类型、国家多维统计计算
├── visualization/ # 可视化绘图模块
│ ├── init.py
│ └── plots.py # 趋势图、饼图、横向柱状图生成
├── output/ # 输出数据目录
│ └── movies.csv # 清洗完毕的结构化数据集
├── app.py # Streamlit 可视化看板入口
├── run_crawler.py # 一键执行爬虫 + 数据清洗脚本
├── config.py # 请求头、URL、超时时间等全局配置
├── requirements.txt # Python 依赖清单
├── .gitignore # Git 忽略文件配置
├── LICENSE # MIT 开源协议
└── README.md # 项目说明文档
> 目录分层清晰，各模块职责单一，完全遵循Python标准化项目布局规范。

---

## 快速开始
### 环境要求
- Python 3.8 及以上版本
- pip 包管理工具

### 安装部署步骤
```bash
# 1. 克隆代码仓库
git clone https://github.com/macheng216/douban-top250-crawler-visualization.git
cd douban-top250-crawler-visualization

# 2. 批量安装项目依赖
pip install -r requirements.txt

# 3. 运行爬虫，抓取并清洗数据
python run_crawler.py

# 4. 启动交互式可视化看板
streamlit run app.py
```
执行完毕浏览器会自动跳转 http://localhost:8501，即可查看完整数据分析看板

## 使用说明
爬虫自定义配置：可在 config.py 修改请求头、超时时间、重试次数、目标爬取地址；
新增数据源扩展：在 crawler/ 目录新建爬虫子类，继承 BaseCrawler 并重写 parse () 方法即可接入新数据源；
看板交互：侧边栏自定义筛选年份区间、最低评分阈值，多标签页切换不同统计图表；
中文兼容：绘图模块内置中文字体配置，若本地无 SimHei 字体，可替换为系统可用中文字体。

## 数据分析洞察示例
基于豆瓣 Top250 数据集挖掘出以下结论：
-📈 90 年代高分影片黄金期：1990-2000 年上映影片数量与平均分整体处于高位；
-🥧 剧情片高分占比最高：评分≥9.0 的影片中，剧情类影片占比超 40%；
-🌍 美国影片数量领先：榜单中美式影片数量断层第一，其次为日本、国产影片；
-💰 票房数据缺失严重：老电影、文艺片无完整票房记录，仅商业院线影片存在有效票房字段。
## 可扩展性设计
项目架构面向生产环境迭代设计，平滑支持大数据量级升级：
维度	当前单机实现	可平滑升级至
计算引擎	Pandas 单机运算	PySpark 分布式计算，业务代码无需重写
数据存储	CSV 本地文件	SQLite/MySQL → Hive/Delta Lake 数据仓库
任务调度	手动执行脚本	Airflow 定时调度，自动更新数据报表
数据源	豆瓣 Top250	TMDB、IMDB 多数据源接入融合
部署方式	本地启动	Docker 容器打包部署至云服务器
实现计算逻辑与执行引擎解耦，数据量从几百条扩张至 TB 级无需重构业务代码。

## 工程规范
项目严格遵循企业级 Python 开发规范：
✅ 代码规范：全部代码遵循 PEP8 编码规范，支持 flake8、pylint 自动化代码校验；
✅ 模块化架构：采集、清洗、分析、可视化分层独立，高内聚低耦合；
✅ 异常与日志：统一 logging 日志记录，异常捕获完备，便于问题排查；
✅ 版本管控：Git 规范管理源码，.gitignore 过滤缓存、虚拟环境、输出数据等冗余文件；
✅ 代码注释：核心函数添加标准 docstring 文档注释，配套完整 README 部署文档。
## 未来规划
 接入 TMDB/IMDB 爬虫，做多源数据融合交叉校验
 数据持久化迁移至 SQLite，支持复杂 SQL 查询统计
 编写 Dockerfile，实现项目一键容器化部署
 接入 Airflow 实现定时增量爬取，自动生成分析报告
 使用 PySpark 重构统计层，验证海量数据分布式运算性能
## 作者
马晨阁
求职方向：Python / 大数据开发实习生
📧 Email: Macheng216@outlook.com
🔗 GitHub: @macheng216
如果本项目对你有参考价值，欢迎点亮 Star ⭐；如有实习、内推机会，欢迎邮件沟通联系。
