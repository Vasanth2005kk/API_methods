import json
from flask import Flask, jsonify, request

app = Flask(__name__)

employees = [
  { 'id': 1, 'name': 'vasanth' },
  { 'id': 2, 'name': 'celine' },
  { 'id': 3, 'name': 'punitha' },
  { 'id': 4, 'name': 'parthi'},
  { 'id': 5, 'name': 'nigi'}
]

nextEmployeeId = len(employees)+1

@app.route('/employees', methods=['GET'])
def get_employees():
  return jsonify(employees)

@app.route('/employees/<int:id>', methods=['GET'])
def get_employee_by_id(id: int):
  employee = get_employee(id)
  if employee is None:
    return jsonify({ 'error': 'Employee does not exist'}), 404
  else:
    return jsonify(employee)

def get_employee(id): # return next((e for e in data if e['id'] == id), None)
  for e in employees:
    if e["id"] == id:
      return e
  return None

def employee_is_valid(employee):
  for key in employee.keys():
    if key != 'name':
      return False
  return True

@app.route('/employees', methods=['POST'])
def create_employee():
  global nextEmployeeId
  employee = json.loads(request.data) #call the post mathode user request the data is proper formate coverting in stord a employee variable
  if not employee_is_valid(employee):
    return jsonify({ 'error': 'Invalid employee properties.' }), 400

  employee['id'] = nextEmployeeId
  nextEmployeeId += 1
  employees.append(employee)

  return jsonify({'post method':"succefully"}), 201 


@app.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id: int):
  employee = get_employee(id)
#   print(employee)
  if employee is None:
    return jsonify({ 'error': 'Employee does not exist.' }), 404

  updated_employee = json.loads(request.data) #call the put mathode user id is url define and updated_employee varible stord json formate 
#   print(updated_employee)
  if not employee_is_valid(updated_employee):
    return jsonify({ 'error': 'Invalid employee properties.' }), 400

  employee.update(updated_employee)
  return jsonify(employee)

@app.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id: int):
  global employees
  employee = get_employee(id)
  if employee is None:
    return jsonify({ 'error': 'Employee does not exist.' }), 404

  employee = []#[e for e in employees if e['id'] != id]
  delete_employee_lits=[]
  for i in employees:
    if i["id"] != id :
      employee.append(i)
    else:
      delete_employee_lits.append(i)
    employees=employee
  return jsonify(delete_employee_lits), 200

if __name__ == "__main__":
  app.run(debug=True)