# 1. Write a function to fetch data from SQL Table via APi
import mysql.connector as conn
from flask import Flask, request, jsonify

app = Flask(__name__)

mydb = conn.connect(host="localhost", user="root", passwd="mysql")
cursor = mydb.cursor()


@app.route("/show_db", methods=["GET", "POST"])
def show_database():
    if request.method == "POST":
        cursor.execute("show databases")
        dbs_name = cursor.fetchall()
        return jsonify(dbs_name)


@app.route("/select_db", methods=["GET","POST"])
def select_database():
    if request.method == "POST":
        dbs_name = request.json["database"]
        try:
            cursor.execute("use {}".format(dbs_name))
        except Exception as e:
            return jsonify("No such database present!", e)
        # once db is selected display all the tables
        cursor.execute("show tables")
        tables = cursor.fetchall()
        return jsonify(tables)


@app.route("/select_all", methods=["GET","POST"])
def select_all():
    if request.method == "POST":
        dbs_name = request.json["database"]
        table = request.json["table"]

        try:
            cursor.execute("use {}".format(dbs_name))
        except Exception as e:
            return jsonify("No such database present!", e)

        try:
            cursor.execute("select * from {}".format(table))
        except Exception as e:
            print("No such table exists! ", e)

        data = cursor.fetchall()
        return jsonify(data)


if __name__ == "__main__":
    app.run()