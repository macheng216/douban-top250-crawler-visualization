# analysis/aggregator.py
import pandas as pd

def load_data(path='output/movies.csv'):
    return pd.read_csv(path)

def yearly_stats(df):
    """每年电影数量、平均评分、平均时长"""
    yearly = df.groupby('year').agg(
        count=('title', 'count'),
        avg_rating=('rating', 'mean'),
        avg_duration=('duration', 'mean')
    ).reset_index()
    yearly['avg_rating'] = yearly['avg_rating'].round(2)
    yearly['avg_duration'] = yearly['avg_duration'].round(1)
    return yearly

def country_distribution(df):
    """国家/地区电影数量统计"""
    # 有些国家字段可能包含多个，如“美国 / 英国”，简单起见我们按第一个国家统计，或者按整个字符串
    # 这里先用完整字符串分组，如果有多国合作会分别计数，后续可视化可以根据需要拆分
    country_counts = df['country'].value_counts().reset_index()
    country_counts.columns = ['country', 'count']
    return country_counts

def genre_distribution(df):
    """拆分类型统计"""
    # genre字段如 "剧情 喜剧 爱情"，拆分后堆叠
    genre_series = df['genre'].str.split(expand=True).stack()
    genre_counts = genre_series.value_counts().reset_index()
    genre_counts.columns = ['genre', 'count']
    return genre_counts

def top_boxoffice(df, top_n=10):
    """票房Top10"""
    return df.nlargest(top_n, 'box_office')[['title', 'year', 'box_office', 'rating']]