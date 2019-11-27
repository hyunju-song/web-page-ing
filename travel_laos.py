import time
from selenium import webdriver
import re



driver = webdriver.Chrome('/Users/songhyeonju/Downloads/chromedriver')
driver.implicitly_wait(2)
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbtravel

data = driver.get('https://www.youtube.com/results?search_query=%EB%9D%BC%EC%98%A4%EC%8A%A4')

time.sleep(3)
Youtube_laos = driver.find_elements_by_css_selector('div#contents')

for laos in Youtube_laos :
    views = laos.find_elements_by_css_selector('div#metadata-line')
    for view in views :
        real_view = view.text

        view_search = re.match('조회수(.+)만회'. real_view)
        print(view_search)

    contents = laos.find_elements_by_css_selector('a#video-title')
    for content in contents :
        real_content = content.text
        print(real_content)




