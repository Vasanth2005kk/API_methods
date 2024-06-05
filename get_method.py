from flask import Flask,jsonify,request

api=Flask(__name__)


# Own api get method
# curl http://127.0.0.1:5000/get

data={
    "name":"vasanth",
    "age":18,
    "cource":"Python",
    "department":"B.Sc Computer Science"
}

@api.route("/get",methods=["GET"])
def get_method():
    return  jsonify(data)

 

if __name__ == "__main__":
    api.run(debug=True)

    # flask run command
    # flask --app get_method run --debug



# get method 
'''
import requests

api_url="https://api.github.com/users/Vasanth2005kk"

ressponce= requests.get(url=api_url)
json_format=ressponce.json()
print(json_format)

'''