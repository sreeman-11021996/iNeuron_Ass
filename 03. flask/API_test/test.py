from flask import Flask, request, jsonify

# create an object of Flask class
app = Flask(__name__)
# __name__ -> referencing this file
# the below function is hosted at this particular route - "\xyz"
# GET method ->  data is sent by appending to the query (
# through url)(data is visible) - google search
# POST method -> data is hidden and sent in the body - any login

@app.route('/xyz',methods = ["GET","POST"])
def test():
    if (request.method == "POST"):
        a = request.json["num1"]
        b = request.json["num2"]
        result = a + b
        return jsonify(result)

if __name__ == "__main__":
    app.run()

# (ip adress[127.0.0.1]) : (port number[5000])/xyz
# (http://127.0.0.1:5000/xyz)
# 400 -> problem from client side
# 500 -> problem from server side
# 404 -> server not found
# 200 -> successful execution

# 1. Write a function to fetch data from SQL Table via APi
# 2. Write a function to fetch data from Mongodb Table via API