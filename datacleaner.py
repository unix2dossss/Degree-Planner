import json
import re

with open('course_data.json', 'r') as data_file:
    data = json.load(data_file)

def parse_course_string(course_string):
    # Remove whitespace and split the string into individual courses
    courses = re.split(r',\s*|\s+and\s+', course_string)

    parsed_courses = []
    for course in courses:
        # Extract the course name and number using regex
        match = re.search(r'([A-Z]+)\s+(\d+)', course)
        if match:
            course_name = match.group(1)
            course_number = match.group(2)
            parsed_courses.append(f"{course_name} {course_number}")

    return parsed_courses

for stage in data.keys():
    print('---')
    print(stage)
    print('---')
    for course in data[stage]:
        if 'Restriction' in data[stage][course].keys():
            print(parse_course_string(data[stage][course]['Restriction']))

'''
Catergories
- Cannot be taken with or after
- Completely Restricted

Filters Required
- Cannot be taken with

'''