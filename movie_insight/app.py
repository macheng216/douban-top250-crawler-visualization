# app.py
import streamlit as st
import pandas as pd
from analysis.aggregator import load_data, yearly_stats, country_distribution, genre_distribution, top_boxoffice
from visualization.plots import plot_yearly_trend, plot_high_rating_genre, plot_country_bar

st.set_page_config(page_title="电影数据分析看板", layout="wide")
st.title("🎬 豆瓣Top250 电影数据可视化分析")

# 加载数据
df = load_data()

# 侧边栏
st.sidebar.header("筛选条件")
min_year, max_year = int(df['year'].min()), int(df['year'].max())
year_range = st.sidebar.slider("年份范围", min_year, max_year, (min_year, max_year))
min_rating = st.sidebar.slider("最低评分", 0.0, 10.0, 0.0, 0.1)

# 筛选数据
filtered_df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1]) & (df['rating'] >= min_rating)]

st.sidebar.markdown(f"当前筛选后共 **{len(filtered_df)}** 部电影")

# 主区域 tab 切换
tab1, tab2, tab3, tab4 = st.tabs(["📈 年度趋势", "🥧 高分类型", "🌍 国家分布", "💰 票房排行"])

with tab1:
    st.subheader("年度电影数量与平均评分趋势")
    yearly = yearly_stats(filtered_df)
    if yearly.empty:
        st.warning("无数据")
    else:
        fig = plot_yearly_trend(yearly)
        st.pyplot(fig)

with tab2:
    st.subheader("高分电影类型分布")
    rating_threshold = st.slider("高分标准", 8.0, 9.5, 9.0, 0.1, key='genre_rating')
    fig = plot_high_rating_genre(filtered_df, rating_threshold)
    st.pyplot(fig)
    st.caption(f"筛选标准：评分≥{rating_threshold}，共{len(filtered_df[filtered_df['rating']>=rating_threshold])}部")

with tab3:
    st.subheader("电影国家/地区分布")
    top_n = st.slider("展示数量", 5, 30, 10)
    fig = plot_country_bar(filtered_df, top_n)
    st.pyplot(fig)

with tab4:
    st.subheader("票房排行榜（亿为单位）")
    n = st.number_input("显示前N", 5, 50, 10)
    top = top_boxoffice(filtered_df, n)
    st.dataframe(top.style.format({'box_office': '{:.2f} 亿', 'rating': '{:.1f}'}))