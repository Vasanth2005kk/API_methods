import requests

name = input("What would you like your employee to be named? ")

post_url="http://localhost:5000/employees"

#  commend line interface (CLI)
#  curl -X POST http://localhost:5000/employees -H "Content-Type: application/json" -d '{ "name" : "praveen" }'

employee = {
    "name": name
    }

headers = {"Content-type": "application/json"}

response = requests.post(post_url, json=employee, headers=headers)
if  response.status_code == 201:
    print(response.json()) 


# print(response.content)
# print(response.headers)
# print(response.status_code)


# example reference code 
'''
from flask import Flask, request, jsonify

app = Flask(__name__)

# post methods
# curl -X POST http://127.0.0.1:5000/post -H "Content-Type: application/json" -d '{"num1": 79, "num2": 3}'

@app.route("/post", methods=["POST"])

def post_method():
    data = request.get_json()
    num1 = data.get('num1')   # num1 = data['num1']
    num2 = data.get('num2')   # num2 = data['num2']
    result = num1 + num2
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
    
    # flask run command
    # flask --app post_method run --debug



data={
  "num1":100,
  "num2":500
}

import requests
api_url = "http://127.0.0.1:5000/post"

response = requests.post(api_url, json=data)
json_formate=response.json()

print(json_formate)

# print(response.status_code)  ==> 200

'''