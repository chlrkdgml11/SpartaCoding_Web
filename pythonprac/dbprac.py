from pymongo import MongoClient
import certifi

ca = certifi.where()
client = MongoClient('mongodb+srv://Kanghee:Rkdgml110^@cluster0.e5sej63.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

doc = {
    'name' : 'bob',
    'age' : 27
}

db.users.insert_one(doc)

