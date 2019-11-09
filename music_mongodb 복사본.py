import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbmusic

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20190908',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

musics = soup.select('#body-content > div.newest-list > div > table > tbody > tr.list')


for music in musics:
    ranking_img = music.select_one('td.number')
    ranking = ranking_img.contents[0].strip()

    title_img = music.select_one('td.check > input')
    title = title_img['title']

    artist_img = music.select_one('td.info > a.artist.ellipsis')
    artist = artist_img.contents[0]

    print(ranking, title, artist)


    db.musics.insert_one({'ranking':ranking, 'title':title, 'artist':artist})
