import requests

id = input("Which employee id do you want to delete? ")
delete_url=f"http://localhost:5000/employees/{id}"

# commend line interface
# curl -X DELETE http://localhost:5000/employees/4 -H "Accept: application/json"

response = requests.delete(delete_url)

print(response.json())