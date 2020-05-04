import requests
from bs4 import BeautifulSoup
url = "http://iiitvadodara.ac.in/faculty.php"


'''AIM: Print names of all the Permanent Faculties'''

r = requests.get(url)
htmlContent = r.content
# print(htmlContent)


soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify)


# target = soup.find('div', class_='content faculty-list')

target = soup.select('div.faculty-list')

for names in target:
    name_list = names.find_all('h3')
    link_list = names.find_all('a')
    # print(name_list)

# print(name_list)

for name in name_list:
    print(name.get_text())


# for nm in names.stripped_stings:
#     print(nm)