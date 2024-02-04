import logging
import re
import traceback
from datetime import datetime, date
from time import sleep

import requests
from bs4 import BeautifulSoup

from utils import start_chrome_session

logging.basicConfig(level=logging.INFO)
MAX_RETRIALS = 10


def get_news_from_wechat(url):
    """
    从微信公众号的合集中爬取消息
    :param url:合集的url
    :return: [title, new_url, publish_date]
    """
    driver = start_chrome_session()
    driver.get(url)
    album_title = driver.find_element_by_css_selector('.album__author-name').text
    logging.info(f"Scraping {album_title}")
    up_to_date = False
    set_date = date.today()
    # This is for test
    # set_date = datetime.strptime('2023-10-01', '%Y-%m-%d').date()
    cur_index, trials = 0, 0
    news = []
    while not up_to_date:
        news_list = driver.find_element_by_css_selector(".album__list.js_album_list")
        news_elements = news_list.find_elements_by_tag_name("li")
        for index in range(cur_index, len(news_elements)):
            try:
                news_title = news_elements[index].get_attribute("data-title")
                news_url = news_elements[index].get_attribute("data-link")
                # open the link and get the date
                response = requests.get(news_url)
                soup = BeautifulSoup(response.text, "html.parser")
                script_tag = soup.find('script', string=re.compile('createTime'))
                pattern = re.compile(r"var createTime = '([^']+)'")
                match = pattern.search(script_tag.text)
                news_date = match.group(1).split()[0]
                news_date = datetime.strptime(news_date, '%Y-%m-%d').date()
                if news_date < set_date:
                    up_to_date = True
                    break
                else:
                    news.append([news_title, news_url, str(news_date)])
                    print(f"\r{album_title} got {len(news)} news.", end='')
            except Exception as e:
                logging.error(f"{e} happen in {album_title}!")
                trials += 1
                if trials > MAX_RETRIALS:
                    traceback.print_exc()
                    up_to_date = True
                    break
        if not up_to_date and cur_index != len(news_elements):
            cur_index = len(news_elements)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(1)
        else:
            # 防止页面到底的新闻仍在时间范围内
            break
    driver.quit()
    return news


def get_news_from_jiqizhixin():
    """
    从机器之心中爬取消息
    :return: [title, new_url, publish_date]
    """
    driver = start_chrome_session()
    url = 'https://jiqizhixin.com/'
    driver.get(url)
    up_to_date = False
    logging.info(f"Scraping {url}")
    set_date = date.today()
    # This is for test
    # set_date = datetime.strptime('2024-01-21', '%Y-%m-%d').date()
    news = []
    cur_index, trials = 0, 0
    while not up_to_date:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(1)
        news_elements = driver.find_elements_by_css_selector('.article-item__title.t-strong.js-open-modal')
        for i in range(cur_index, len(news_elements)):
            try:
                news_title = news_elements[i].text
                news_url = news_elements[i].get_attribute('href')
                news_date = news_url.split('/')[-1][:10]
                news_date = datetime.strptime(news_date, '%Y-%m-%d').date()
                if news_date < set_date:
                    up_to_date = True
                    break
                else:
                    news.append([news_title, news_url, str(news_date)])
                    print(f"\rJiqizhixin got {len(news)} news.", end='')
            except Exception as e:
                logging.error(f"{e} happen in {url}!")
                trials += 1
                if trials > MAX_RETRIALS:
                    traceback.print_exc()
                    up_to_date = True
                    break
        if not up_to_date and cur_index != len(news_elements):
            cur_index = len(news_elements)
            btn = driver.find_element_by_css_selector(".u-loadmore")
            btn.click()
        else:
            # 防止页面到底的新闻仍在时间范围内
            break
    driver.quit()
    return news


if __name__ == '__main__':
    # url = 'https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzU1MzY0MDI2NA==&action=getalbum&album_id=1562988036857053186&scene=173&subscene=93&sessionid=1705627760&enterid=1705627950&from_msgid=2247504883&from_itemidx=1&count=3&nolastread=1#wechat_redirect'
    url = 'https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzIwMjAwMjk4Mg==&action=getalbum&album_id=3079598529188298756&scene=126#wechat_redirect'
    news = get_news_from_wechat(url)
    print(news)
    news = get_news_from_jiqizhixin()
    print(news)
