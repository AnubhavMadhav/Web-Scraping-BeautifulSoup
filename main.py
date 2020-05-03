# Step 0:
# Install requirements
# pip install requests
# pip install html5lib
# pip install bs4

import requests
from bs4 import BeautifulSoup
url = "https://www.codewithharry.com/"


# Step 1:
# Get the HTML
r = requests.get(url)
htmlContent = r.content
# print(htmlContent)



# Step 2:
# Parse HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup)
# print(soup.prettify)


# Step 3:
# HTML Tree Traversal

# Commonly used type of objects
# 1. Tag
# 2. NavigableString
# 3. BeautifulSoup
# 4. Comment

# Get the title of HTML Page
title = soup.title

# print(type(soup))               # <class 'bs4.BeautifulSoup'>
# print(type(title))              # <class 'bs4.element.Tag'>
# print(type(title.string))       # <class 'bs4.element.NavigableString'>


# Get all the paragraphs from HTML
paras = soup.find_all('p')
print(paras)