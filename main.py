import json
from graph.ADT import Graph, Tree

# Load data from the JSON file
with open('data.json', 'r') as file:
    data = json.load(file)


for course_id, course_info in data.items():
    print(f"ID: {course_id}")
    print(f"Code: {course_info['code']}")
    print(f"Name: {course_info['name']}")
    print(f"Description: {course_info['description']}")
    print(f"Prerequisites: {', '.join(str(p) for p in course_info['prerequisites'])}" if course_info['prerequisites'] else "Prerequisites: None")
    print(f"Restrictions: {', '.join(course_info['restrictions'])}" if course_info['restrictions'] else "Restrictions: None")
    print(f"Stage: {course_info['stage']}")
    print()

courses = []

def prompt_user():
    for i in range(4):
        selection = input('Select Course: ')
        if selection == 'exit':
            break
        course = Graph(selection, data[selection]['code'], data[selection]['description'], data[selection]['prerequisites'], data[selection]['restrictions'], data[selection]['stage'])
        courses.append(course)

        print(courses)

    for c in courses:
        print(c.id, c.code, c.description, c.restrictions, c.prerequisites, c.stage)

prompt_user()
prompt_user()

# for course in courses = 