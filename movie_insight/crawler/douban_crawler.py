# crawler/douban_crawler.py
import re
import logging
import time
import random
from lxml import etree
from .base_crawler import BaseCrawler
from config import BASE_URL


class DoubanTop250Crawler(BaseCrawler):
    def parse(self, html):
        tree = etree.HTML(html)
        items = tree.xpath('//div[@class="item"]')
        movies = []
        for item in items:
            # 片名
            titles = item.xpath('.//div[@class="hd"]/a/span[@class="title"]/text()')
            title = titles[0].strip() if titles else ''

            # 评分
            rating_num = item.xpath('.//span[@class="rating_num"]/text()')
            rating = float(rating_num[0]) if rating_num else None

            # 评价人数
            rating_people = item.xpath('.//div[@class="star"]/span[last()]/text()')
            people = 0
            if rating_people:
                people_str = rating_people[0]
                people = int(re.sub(r'\D', '', people_str))  # 提取数字

            # 详细信息段落
            info_p = item.xpath('.//div[@class="bd"]/p[1]/text()')
            info_text = ''.join(info_p).strip() if info_p else ''

            # 用正则从info_text中抽取导演、年份、国家、类型
            # 示例："导演: 弗兰克·德拉邦特 Frank Darabont  主演: ... 1994 / 美国 / 犯罪 剧情"
            # 年份
            year_match = re.search(r'(\d{4})', info_text)
            year = int(year_match.group(1)) if year_match else None

            # 国家/地区
            # 年份之后跟着 /国家/ 类型
            parts = [p.strip() for p in info_text.split('/')]
            if len(parts) >= 2:
                # 倒数第二部分通常是国家
                country = parts[-2].strip()
            else:
                country = ''

            # 类型：最后一部分
            genre_str = parts[-1].strip() if parts else ''

            # 时长：在info_text中或者另一个p里可能有，比如 "139分钟"
            duration_match = re.search(r'(\d+)\s*分钟', info_text)
            duration = int(duration_match.group(1)) if duration_match else None

            # 票房：通常也在info_text中，形式如 "票房: $2.8亿" 或 "票房: ￥2.8亿"
            box_office = None
            bo_match = re.search(r'票房:\s*[￥$]?([\d.]+)(亿|万)?', info_text)
            if bo_match:
                num = float(bo_match.group(1))
                unit = bo_match.group(2)
                if unit == '亿':
                    pass
                elif unit == '万':
                    num /= 10000
                # 如果不带单位则默认是万？实际情况多数带单位，这里简单处理
                box_office = num  # 单位：亿

            movies.append({
                'title': title,
                'rating': rating,
                'people': people,
                'year': year,
                'country': country,
                'genre': genre_str,
                'duration': duration,
                'box_office': box_office
            })
        return movies

    def crawl_all(self):
        all_movies = []
        for start in range(0, 250, 25):
            url = f"{BASE_URL}?start={start}"
            logging.info(f"正在爬取: {url}")
            page_movies = self.crawl(url)
            all_movies.extend(page_movies)
            time.sleep(random.uniform(1, 3))  # 礼貌爬取
        return all_movies
