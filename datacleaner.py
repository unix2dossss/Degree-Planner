"""
Add few restrictions in Stage I manually into output json.
"""

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

all_courses = []

for stage in data.keys():
    for course in data[stage]:
        all_courses.append(course)

def course_restriction_range_finder(restriction_string):
    cannot_take_courses = []
    # Extract individual courses
    courses = re.findall(r'COMPSCI \d+', restriction_string)
    cannot_take_courses.extend(courses)

    # Extract course ranges
    ranges = re.findall(r'(\d+)-(\d+)', restriction_string)
    
    for start, end in ranges:
        start = int(start)
        end = int(end)
        for course in all_courses:
            course_number = re.findall(r'\d+', course)[0]  # Extract numeric course number
            if start <= int(course_number) <= end:
                cannot_take_courses.append(course)
    
    return cannot_take_courses


for stage in data.keys():
    print('---')
    print(stage)
    print('---')
    for course in data[stage]:
        if 'Restriction' in data[stage][course].keys():
            if 'Cannot be taken with' in data[stage][course]['Restriction']:
                # print(data[stage][course]['Restriction'])
                rs = course_restriction_range_finder(data[stage][course]['Restriction'])
                data[stage][course]['Take Before'] = rs
            else:
                data[stage][course]['Restriction'] = parse_course_string(data[stage][course]['Restriction'])


json_str = json.dumps(data, indent=4)
print(json_str)

'''
Catergories
- Cannot be taken with or after
- Completely Restricted

Filters Required
- Cannot be taken with
'''