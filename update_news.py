from datetime import date
from multiprocessing import Pool

import pandas as pd

from tools.spiders import get_news_from_wechat, get_news_from_jiqizhixin
from utils import read_json


def update_news():
    """
    更新新闻存入excel中
    :return:
    """
    wechat_infos = read_json('./configs/wechat_urls.json')
    wechat_urls = []
    for info in wechat_infos:
        wechat_urls.append(info['url'])
    res = []
    with Pool() as pool:
        wechat_res = pool.map_async(get_news_from_wechat, wechat_urls)
        jiqizhixin_res = pool.apply_async(get_news_from_jiqizhixin)
        wechat_news_list = wechat_res.get()
        jiqizhixin_news = jiqizhixin_res.get()
    for wechat_news in wechat_news_list:
        res.extend(wechat_news)
    res.extend(jiqizhixin_news)
    res_df = pd.DataFrame(res, columns=["title", "url", "date"])
    res_df.to_excel(f'./database/{str(date.today())}_news.xlsx', index=False)


if __name__ == '__main__':
    update_news()
