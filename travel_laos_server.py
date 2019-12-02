import random
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbtravel
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
import requests

## HTML을 주는 부분
@app.route('/')
def home():
   # get youtube db
   youtube_laos = list(db.laos_youtube.find({}, {'_id': False}))
   blog_laos = list(db.laos_blog.find({}, {'_id' : False}))
   print(youtube_laos)
   print(blog_laos)

   youtube_items = random.choices(youtube_laos, k=3)
   blog_items = random.choices(blog_laos, k=3)

   return render_template('travel_laos.html', youtube_items=youtube_items, blog_items=blog_items)



if __name__ == '__main__':
   app.run('0.0.0.0', port=5000,debug=True)
