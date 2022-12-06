from pymongo import MongoClient
import certifi

ca = certifi.where()
client = MongoClient('mongodb+srv://Kanghee:Rkdgml110^@cluster0.e5sej63.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

movie = db.movies.find_one({'title': '가버나움'})

print(movie['star'])

find_movies = list(db.movies.find({'star' : movie['star']}, {'_id' : False}))

for s in find_movies:
    print(s['title'])

db.movies.update_one({'title' : '가버나움'}, {'$set' : {'star' : '0'}})