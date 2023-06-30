from bs4 import BeautifulSoup
import requests
import json

url = "https://www.calendar.auckland.ac.nz/en/courses/faculty-of-science/computer-science.html"
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
# print(doc.prettify())

divs = doc.find_all('div', class_='courseStage section')

print(len(divs))