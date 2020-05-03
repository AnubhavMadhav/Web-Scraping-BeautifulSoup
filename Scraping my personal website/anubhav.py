import requests
from bs4 import BeautifulSoup
url = "https://anubhavmadhav.github.io/Anubhav-Madhav/"
url2 = "https://anubhavmadhav.github.io/Anubhav-Madhav/projects.html"

r = requests.get(url)
r2 = requests.get(url2)
htmlContent = r.content
htmlContent2 = r2.content
# print(htmlContent)
# print(htmlContent2)

soup = BeautifulSoup(htmlContent, 'html.parser')
soup2 = BeautifulSoup(htmlContent2, 'html.parser')
# print(soup)
# print(soup.prettify)

title = soup.title
# print(title)

title2 = soup2.title
# print(title2)


divs = soup.find_all('div')
# print(divs)

# First h3
# print(soup.find('h3'))


# print(soup.find('div')['class'])


# print(soup.find('div', class_='intro'))


# print(soup.find('div', class_='intro').get_text())

anchors = soup.find_all('a')
all_links = set()

for link in anchors:
    linkText = "https://anubhavmadhav.github.io/Anubhav-Madhav" + link.get('href')
    all_links.add(linkText)
    # print(linkText)

# print(all_links)


targetis = soup2.find(class_='projects')
# print(targetis)
# print(targetis.contents)
targetchild = targetis.children
# print(targetchild)

for child in targetchild:
    pass
    # print(child)


for item in targetis.strings:
    pass
    # print(item)

for item in targetis.stripped_strings:
    # print(item)
    pass

target2 = soup2.find(class_='project5')
# print(target2)
# print(target2.previous_sibling.previous_sibling)
# print(target2.parent.name)
# print(target2.previous_sibling.previous_sibling.name)




'''Print the Name of all Projects Completed by Anubhav Madhav along with all the links in projects div'''

main2 = soup2.select('div.projects')[0]
# print(main2)
    # print(main2)
    # exit()
linkos=set()
names2=[]
for itemize in main2.find_all('h1'):
    for linkes in main2.find_all('a'):
        linkies = linkes.get('href')
        linkos.add(linkies)
    names = itemize.get_text()
    print(names)
    names2.append(names)

# names2.sort()
        # print(linkies)
# print(names)
linkos2 = list(linkos)
for linkos3 in linkos2:
    print(linkos3)
#
# dic = {}
#
# for key in names2:
#     for value in linkos2:
#         dic[key] = value
#         linkos2.remove(value)
#         break
#
# print(dic)

