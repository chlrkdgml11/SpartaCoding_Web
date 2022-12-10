from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import certifi

ca = certifi.where()
client = MongoClient('mongodb+srv://Kanghee:Rkdgml110^@cluster0.e5sej63.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/test', methods=['GET'])
def test_get():
    title_receive = request.args.get('title_give')
    print(title_receive)
    return jsonify({'result': 'success', 'msg': '이 요청은 GET!'})