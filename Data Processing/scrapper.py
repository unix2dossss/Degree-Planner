from bs4 import BeautifulSoup
import requests
import json

data = dict()

url = "https://www.calendar.auckland.ac.nz/en/courses/faculty-of-science/computer-science.html"
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
# print(doc.prettify())

divs = doc.find_all('div', class_='courseStage section')

for stage in divs:
    # Finds Stage Number/Title. | Example: Stage I
    stage_part = stage.find('h3', class_='stage').text.strip()
    data[stage_part] = dict()
    
    courses_div = stage.find_all('div', class_='coursePaper section')
    for course in courses_div:
        # Finds Course Code Number | Example: COMPSCI 101
        course_code = course.find('div', class_='courseA').text.strip()
        data[stage_part][course_code] = dict()

        # Finds Course Name | Example: Principles of Programming
        course_name = course.find('p', class_='title').text.strip()
        data[stage_part][course_code]["Name"] = course_name

        # Finds Course Description | Example: A practical introduction to computers ...
        course_description = course.find('p', class_='description').text.strip()
        data[stage_part][course_code]["Description"] = course_description

        restrictions_list = course.find_all('p', class_='prerequisite')
        # print(restrictions_list)
        for restrictions in restrictions_list:
            if restrictions != None:
                restrictions_data = restrictions.text.split()
                if restrictions_data[0] == 'Restriction:':
                    restrictions_string = " ".join(restrictions_data[1:])
                    data[stage_part][course_code]['Restriction'] = restrictions_string
                if restrictions_data[0] == 'Prerequisite:':
                    restrictions_string = " ".join(restrictions_data[1:])
                    data[stage_part][course_code]['Prerequisite'] = restrictions_string


json_str = json.dumps(data, indent=4)
print(json_str)

with open("course_data.json", "w" ) as file:
    json.dump(data, file)