from flask import Flask, request, jsonify

app = Flask(__name__)
CONNECTION_STRING = "mongodb://hren_db_1:27017"
from pymongo import MongoClient
client = MongoClient(CONNECTION_STRING)

def get_database():
    return client['db_1']

@app.route('/')
def hello_world():
    return 'Hello Worldyuiyuiyiy!'

@app.route('/pdr', methods=['POST'])
def pdr():
    connection_mongo_db = client.db.db_1
    name = request.json['name']
    id = request.json['id']
    connection_mongo_db.insert({'id': id,
                                'name': name})
    return 'succsess'

@app.route('/one/<i>', methods=['GET'])
def find_one_id(i):
    connection_mongo_db = client.db.db_1
    find_ok = connection_mongo_db.find_one({"id": (i)})
    return str(find_ok)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
