from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")  # Enables headless mode
chrome_options.add_argument("--disable-gpu")  # Disables GPU hardware acceleration; may not be necessary


# 设置浏览器驱动
driver = webdriver.Chrome('../driver/chromedriver.exe', options=chrome_options) # 替换为你的驱动路径

url = "https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzU1MzY0MDI2NA==&action=getalbum&album_id=1562988036857053186&scene=173&subscene=93&sessionid=1705627760&enterid=1705627950&from_msgid=2247504883&from_itemidx=1&count=3&nolastread=1#wechat_redirect"

# 打开网页
driver.get(url)

title = driver.title

# submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
# for _ in range(10):
#     sleep(1)
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# elements = driver.find_elements_by_css_selector(".album__list-item.js_album_item.js_wx_tap_highlight.wx_tap_cell")
news_list = driver.find_element_by_css_selector(".album__list.js_album_list")
elements = news_list.find_elements_by_tag_name("li")
print(elements[0])
print(elements[-1])

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(1)

elements = news_list.find_elements_by_tag_name("li")

print(elements[0])
print(elements[-1])
# text_box.send_keys("Selenium")
# submit_button.click()
# print(news)
# text = message.text
url_list = []
for element in elements:
    print(element.get_attribute('data-title'))
    print(element.get_attribute('data-link'))
    news_url = element.get_attribute('data-link')
    url_list.append(news_url)
for news_url in url_list:
    sleep(1)
    driver.get(news_url)
    date = driver.find_element_by_id("publish_time").text
    print(date.split()[0])
driver.quit()