# data/cleaner.py
import pandas as pd

def clean_movies(movies):
    df = pd.DataFrame(movies)
    # 票房为None的填充0
    df['box_office'] = df['box_office'].fillna(0)
    # 时长缺失也填0或中位数，这里先填0
    df['duration'] = df['duration'].fillna(0).astype(int)
    # 国家字段可能包含多余空格
    df['country'] = df['country'].str.strip()
    # 类型字符串分割成列表方便后续统计，但保留原始字符串
    # 年份为空的丢弃（应该不会有）
    df.dropna(subset=['year'], inplace=True)
    df['year'] = df['year'].astype(int)
    return df