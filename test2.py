from flask import Flask, request, jsonify
import logging
import pymongo
logging.basicConfig(filename="flsk.log", level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')
client = pymongo.MongoClient("mongodb+srv://siva_surya:Kiranteja28@cluster0.y0vj4.mongodb.net/?retryWrites=true&w=majority")
database = client['Flsk']
collection = database['prac']

app = Flask(__name__)


@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        try:
            name = request.json['name']
            number = request.json['number']
            collection.insert_one({name:number})
            logging.info("inserted one document")
        except Exception as e:
            logging.info(e)
    return jsonify(str("document inserted"))


@app.route('/update', methods=['POST'])
def update():
    if request.method == 'POST':
        try:
            names=request.json['names']
            number = request.json['number']
            update_number = request.json['update_number']
            collection.update_many({'{}'.format(names):'{}'.format(number)} , {"$set":{'{}'.format(names):'{}'.format(update_number)}})
            logging.info("updated successfully")
        except Exception as e:
            logging.info(e)
    return jsonify(str("Document updated"))


@app.route('/delete', methods=['POST'])
def delete():
    if request.method == 'POST':
        try:
            name = request.json['name']
            number = request.json['number']

            collection.delete_one({name:number})
            logging.info("deleted successfully")
        except Exception as e:
            logging.info(e)
    return jsonify(str("Document deleted"))


if __name__ == '__main__':
    app.run(debug=True, port=5002)
