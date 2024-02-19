import json

file_path = 'data.json'

with open(file_path, 'r') as file:
    data = json.load(file)

sem1 = ['COMPSCI 101', 'COMPSCI 110', 'COMPSCI 210', 'COMPSCI 120']
