from time import sleep

from selenium import webdriver

driver = webdriver.Chrome('../driver/chromedriver.exe') # 替换为你的驱动路径

url = 'https://jiqizhixin.com/'

driver.get(url)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

sleep(1)

for _ in range(10):
    sleep(1)
    btn = driver.find_element_by_css_selector(".u-loadmore")
    btn.click()

elements = driver.find_elements_by_css_selector(".article-item__title.t-strong.js-open-modal")

for element in elements:
    print(element.text)
    news_url = element.get_attribute('href')
    print(news_url)
    date = element.get_attribute('href').split('/')[-1][:10]
    print(date)

driver.quit()
