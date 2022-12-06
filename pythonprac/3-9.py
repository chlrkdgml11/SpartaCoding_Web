from bs4 import BeautifulSoup
import requests

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20210829',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

movies = soup.select('#old_content > table > tbody > tr')

for movie in movies:
    temp_rank = movie.select_one('td:nth-child(1) > img')
    temp_name = movie.select_one('td.title > div > a')
    temp_star = movie.select_one('td.point')

    if(temp_rank and temp_name and temp_star):
        print(temp_rank['alt'], temp_name['title'], temp_star.text)
