from flask import Flask, request, jsonify
import mysql.connector as conn
mydb = conn.connect(host="localhost", user="root", passwd="Sivasurya28")
cursor = mydb.cursor()
cursor.execute("create database if not exists flk_prac")
cursor.execute("create table if not exists flk_prac.prac(name varchar(20),number int(10))")


app = Flask(__name__)


@app.route('/insert', methods=['POST'])
def insert():
    if request.method=='POST':
        try:
            name = request.json['name']
            number = int(request.json['number'])
            cursor.execute("insert into flk_prac.prac values(%s,%s)",(name,number))
            mydb.commit()
        except Exception as e:
            return jsonify(str(e))
    return jsonify(str("successfully inserted"))


@app.route('/update', methods=['POST'])
def update():
    if request.method == 'POST':
        try:
            get_name = request.json['get_name']
            cursor.execute("update flk_prac.prac set number=10000 where name = %s",(get_name,))
            mydb.commit()
        except Exception as e:
            return jsonify(str(e))
        return jsonify(str("successfully updated"))


@app.route('/delete', methods=['POST'])
def delete():
    if request.method == 'POST':
        try:
            name_del = request.json['name_del']
            cursor.execute("delete from flk_prac.prac where name = %s", (name_del,))
            mydb.commit()
        except Exception as e:
            return jsonify(str(e))
    return jsonify(str("deleted successfully"))


@app.route('/fetch', methods=['POST'])
def fetch():
    if request.method == 'POST':
        try:
            database_name = request.json['database_name']
            table_name = request.json['table_name']
            cursor.execute("select * from {}.{}".format(database_name,table_name))
            data = []
            for i in cursor.fetchall():
                data.append(i)
            return jsonify(str(data))
        except Exception as e:
            return jsonify(str(e))
    return jsonify(str("fetched successfully"))


if __name__ == '__main__':

    app.run(debug=True, port=5001)