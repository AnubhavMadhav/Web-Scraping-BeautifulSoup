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
print(soup)
# Step 3:
# HTML Tree Traversal