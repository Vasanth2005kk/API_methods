import requests


_id=int(input("Which employee id do you want to get ?:"))
get_url=f"http://127.0.0.1:5000/employees/{_id}"

# commend line interface (CLI)
# curl http://127.0.0.1:5000/employees/2

responce=requests.get(get_url)
if responce.status_code == 200:
    json_formate=responce.json()
    print(json_formate)
else:
    print(({ 'error': 'Employee does not exist'}),404)