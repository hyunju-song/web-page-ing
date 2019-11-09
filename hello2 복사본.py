import requests
from bs4 import BeautifulSoup


headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20190909',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

movies = soup.select('table.list_ranking>tbody>tr')

for movie in movies:
    ranking_image = movie.find('img')
    if ranking_image == None:
        continue

    ranking = ranking_image['alt']
    title = movie.select('.title> .tit5> a')[0].get_text()
    rating = movie.select('.point')[0].get_text()

    print(ranking, title, rating)

