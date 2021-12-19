#Web Scraping Using Beautiful Soup. Reads an HTML File and then prints the details.
from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    html_content = html_file.read()

soup = BeautifulSoup(html_content,"lxml")

find_all = soup.find_all('div', class_='card')
Course_Cards = find_all


for course in Course_Cards:
    course_name = course.h5.text
    course_price = course.a.text.split()[-1]
    print("Course name {} and is priced at {}".format(course_name,course_price))
