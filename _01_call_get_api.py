import requests

get_url="http://127.0.0.1:5000/employees" 

# commend line interface (CLI)
# curl http://127.0.0.1:5000/employees

response=requests.get(get_url)
if response.status_code == 200:
    json_formate=response.json()
    print(json_formate)

# status_code=response.status_code #output ==> 200
# print(status_code)
# print(response.headers["Content-Type"]) #output ==> 'application/json; charset=utf-8'