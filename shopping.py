from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta



@app.route('/')
def home():
    return render_template('index.html')



@app.route('/orders', methods=['POST'])
def write_orders():
    name_receive = request.form['name_give']
    count_receive = request.form['count_give']
    address_receive = request.form['address_give']
    phone_receive = request.form['phone_give']


    order = {
        'name': name_receive,
        'count': count_receive,
        'address': address_receive,
        'phone': phone_receive
    }

    db.orders.insert_one(order)
    return jsonify({'result': 'success', 'msg': '주문완료!'})


@app.route('/orders', methods=['GET'])
def read_orders():
    orders = list(db.orders.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'orders': orders})


if __name__ == '__main__':
    app.run('127.0.0.1', port=5000, debug=True)
