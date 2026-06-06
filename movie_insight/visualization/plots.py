# visualization/plots.py
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei']  # 中文支持
matplotlib.rcParams['axes.unicode_minus'] = False

def plot_yearly_trend(yearly_df):
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.bar(yearly_df['year'], yearly_df['count'], color='skyblue', label='电影数量')
    ax.set_xlabel('年份')
    ax.set_ylabel('数量')
    ax.set_title('豆瓣Top250 每年电影数量趋势')
    # 添加平均评分折线
    ax2 = ax.twinx()
    ax2.plot(yearly_df['year'], yearly_df['avg_rating'], 'r-o', label='平均评分')
    ax2.set_ylabel('平均评分')
    lines1, labels1 = ax.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
    plt.tight_layout()
    return fig

def plot_high_rating_genre(df, rating_threshold=9.0):
    high_rated = df[df['rating'] >= rating_threshold]
    # 拆分类型
    genres = high_rated['genre'].str.split(expand=True).stack()
    genre_counts = genres.value_counts()
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(genre_counts.values, labels=genre_counts.index, autopct='%1.1f%%', startangle=90)
    ax.set_title(f'评分≥{rating_threshold}的电影类型分布')
    return fig

def plot_country_bar(df, top_n=10):
    country_counts = df['country'].value_counts().head(top_n)
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(country_counts.index, country_counts.values, color='coral')
    ax.set_xlabel('电影数量')
    ax.set_title(f'Top{top_n} 国家/地区电影数量')
    ax.invert_yaxis()
    return fig