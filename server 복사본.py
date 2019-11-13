from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
import requests

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbshop

@app.route('/')
def home():
   return render_template('index.html')

## API 역할을 하는 부분
@app.route('/order', methods=['POST'])
def order_post():
   name_receive = request.form['name_give']
   count_receive = request.form['count_give']
   address_receive = request.form['address_give']
   phone_receive = request.form['phone_give']
   item_receive = request.form['item_give']
   order_info = {'name':name_receive,'count': count_receive, 'address': address_receive ,
                        'phone': phone_receive, 'item': item_receive}
   db.order.insert_one(order_info)
   return jsonify({'result':'success'})

@app.route('/order', methods=['GET'])
def order_get():
   item_receive = request.args.get('item_give')
   order_info = list(db.order.find({'item': item_receive}, {'_id': 0}))

   return jsonify({'result': 'success', 'orders': order_info })



if __name__ == '__main__':
   app.run('127.0.0.1',port=2000, debug=True)