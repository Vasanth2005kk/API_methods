import requests

_id = int(input("Which employee id would you like to be updated? :"))
name = input("What would you like your employee's name to be changed to? :")

put_url=f"http://localhost:5000/employees/{_id}"

# commend line interface (CLI)
# curl -X PUT -H "Content-Type: application/json" -d '{"name":"vasanthavel"}' "http://localhost:5000/employees/1"

employee = {
    "name": name
    }

headers = {'Content-Type': 'application/json; charset=utf-8'}

response=requests.put(url=put_url,json=employee,headers=headers)

print(response.json())
