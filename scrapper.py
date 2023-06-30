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
    # Finds Course Code Number | Example: COMPSCI 101
    courses_div = stage.find_all('div', class_='coursePaper section')
    for course in courses_div:
        course_code = course.find('div', class_='courseA').text.strip()
        data[stage_part][course_code] = dict()

print(data)

# with open("course_data.json", "w" ) as file:
#     pass