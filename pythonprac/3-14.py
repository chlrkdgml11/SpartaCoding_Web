from bs4 import BeautifulSoup
import requests
from pymongo import MongoClient
import certifi

ca = certifi.where()
client = MongoClient('mongodb+srv://Kanghee:Rkdgml110^@cluster0.e5sej63.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20210829',headers=headers)


soup = BeautifulSoup(data.text, 'html.parser')

movies = soup.select('#old_content > table > tbody > tr')

for movie in movies:
    temp_rank = movie.select_one('td:nth-child(1) > img')
    temp_title = movie.select_one('td.title > div > a')
    temp_star = movie.select_one('td.point')

    if(temp_rank and temp_title and temp_star):
        doc = {
            'title' : temp_title['title'],
            'rank' : temp_rank['alt'],
            'star' : temp_star.text
        }

        db.movies.insert_one(doc)
