# crawler/base_crawler.py
import requests
import time
import random
import logging
from abc import ABC, abstractmethod
from config import HEADERS, REQUEST_TIMEOUT, RETRY_TIMES

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

class BaseCrawler(ABC):
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(HEADERS)

    def fetch(self, url, params=None):
        """带重试机制的请求方法"""
        for attempt in range(1, RETRY_TIMES + 1):
            try:
                resp = self.session.get(url, params=params, timeout=REQUEST_TIMEOUT)
                resp.raise_for_status()
                resp.encoding = resp.apparent_encoding  # 自动处理编码
                return resp.text
            except requests.RequestException as e:
                logging.warning(f"第{attempt}次请求失败: {e}")
                if attempt == RETRY_TIMES:
                    logging.error(f"达到最大重试次数，放弃请求: {url}")
                    raise
                # 指数退避 + 随机延迟
                sleep_time = 2 ** attempt + random.uniform(0, 1)
                time.sleep(sleep_time)

    @abstractmethod
    def parse(self, html):
        """子类必须实现的解析方法"""
        pass

    def crawl(self, url, params=None):
        html = self.fetch(url, params)
        return self.parse(html)