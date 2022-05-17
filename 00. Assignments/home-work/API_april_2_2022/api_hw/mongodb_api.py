# 2. Write a function to fetch data from Mongodb Table via API
import pymongo
from flask import Flask, request, jsonify
from bson import json_util
import json

app = Flask(__name__)

client = pymongo.MongoClient(
    "mongodb+srv://mongodb:mongodb@sreeman.jzldx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",
    tls=True, tlsAllowInvalidCertificates=True)


@app.route("/mongodb/show_db", methods=["GET", "POST"])
def show_databases():
    if request.method == "POST":
        dbs = client.list_database_names()
        return jsonify(dbs)


@app.route("/mongodb/select_db", methods=["GET", "POST"])
def select_database():
    if request.method == "POST":
        db_name = request.json["database"]
        db = client[db_name]
        # show collections:
        cols = db.list_collection_names()
        if len(cols) == 0:
            return jsonify("New Database")
        else:
            return jsonify(cols)


@app.route("/mongodb/select_all", methods=["GET", "POST"])
def select_all():
    if request.method == "POST":
        db_name = request.json["database"]
        db = client[db_name]
        col_name = request.json["collection"]
        col = db[col_name]

        data = col.find()
        response = list()
        for i in data:
            response.append(i)
# 1. Using json_util.dumps() from bson to covert ObjectId in BSON
# response to JSON compatible format
# i.e. "_id": {"$oid": "123456789"} The above JSON Response obtained
# from json_util.dumps() will have backslashes and quotes

# 2. To remove backslashes and quotes use json.loads() from json
        # bson -> json
        json_with_backslashes = json_util.dumps(response)
        json_data = json.loads(json_with_backslashes)

        return jsonify(json_data)


if __name__ == "__main__":
    app.run()
