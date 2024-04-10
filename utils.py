from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import json


def read_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def write_json(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def start_chrome_session(version):
    """
    根据版本启动chrome
    :param version: '120'或'123'
    :return:
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(f"./driver/{version}/chromedriver.exe", chrome_options=chrome_options)
    return driver
