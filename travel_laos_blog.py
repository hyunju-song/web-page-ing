import time
from selenium import webdriver
import re
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome('/Users/songhyeonju/Downloads/chromedriver')
driver.implicitly_wait(2)
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbtravel

for i in range(5):
    start_index = i * 10 + 1
    datas = driver.get('https://search.naver.com/search.naver?date_from=&date_option=0&date_to=&dup_remove=1&nso=&post_blogurl=&post_blogurl_without=&query=%EB%9D%BC%EC%98%A4%EC%8A%A4&sm=tab_pge&srchby=all&st=sim&where=post&start=' + str(start_index))

    time.sleep(3)

    contents = driver.find_elements_by_css_selector('li.sh_blog_top')

    for content in contents:
        dates = content.find_element_by_css_selector('dd.txt_inline')
        real_date = dates.text
        print(real_date)

        title = content.find_element_by_css_selector('a.sh_blog_title._sp_each_url._sp_each_title')
        real_title = title.get_attribute('title')
        print(real_title)

        thumbnail = content.find_element_by_tag_name('img')
        real_img = thumbnail.get_attribute('src')
        print(real_img)

        url = content.find_element_by_tag_name('a')
        real_url = url.get_attribute('href')
        print(real_url)

        db.laos_blog.insert_one({'thumbnail': real_img, 'contents': real_title, 'date': real_date, 'url': real_url})