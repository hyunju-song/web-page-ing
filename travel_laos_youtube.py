import time
from selenium import webdriver
import re
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome('/Users/songhyeonju/Downloads/chromedriver')
driver.implicitly_wait(2)
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbtravel


data = driver.get('https://www.youtube.com/results?search_query=%EB%9D%BC%EC%98%A4%EC%8A%A4')

time.sleep(3)

body = driver.find_element_by_tag_name('body')
for i in range(50):
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)

videos = driver.find_elements_by_tag_name('ytd-video-renderer')

for video in videos:
    view = video.find_element_by_css_selector('div#metadata-line')
    real_view = view.text

    P = re.compile('조회수 (\d+)만회')
    result = P.search(real_view)
    if result:
        view_search = result.group(1)
        view_num = int(view_search) * 10000

        if view_num > 100000:
            view_tenthd = view_num
            print (view_tenthd)

            content = video.find_element_by_css_selector('a#video-title')
            real_content = content.text
            print(real_content)

            thumbnail = video.find_element_by_css_selector('img#img')
            real_img = thumbnail.get_attribute('src')
            print(real_img)

            url = video.find_element_by_css_selector('a#thumbnail')
            real_url = url.get_attribute('href')
            print(real_url)

            db.laos_youtube.insert_one({'thumbnail': real_img, 'contents': real_content, 'view': view_tenthd, 'url': real_url})





