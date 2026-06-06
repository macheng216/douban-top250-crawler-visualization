# run_crawler.py
from crawler.douban_crawler import DoubanTop250Crawler
from data.cleaner import clean_movies
from save_data import save_to_csv
import pandas as pd
import os

def main():
    crawler = DoubanTop250Crawler()
    raw_movies = crawler.crawl_all()
    df = clean_movies(raw_movies)
    os.makedirs('output', exist_ok=True)
    df.to_csv('output/movies.csv', index=False, encoding='utf-8-sig')
    save_to_csv(df.to_dict("records"))
    print(f"成功爬取并保存 {len(df)} 条电影数据。")


if __name__ == '__main__':
    main()