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
    # Finds Stage Number/Title.
    stage_part = stage.find('h3', class_='stage').text.strip()
    data[stage_part] = dict()

print(data)

# print(data)

# with open("course_data.json", "w" ) as file:
#     pass