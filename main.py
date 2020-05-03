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
# print(paras)

# Get all the anchor tags from HTML Page
anchors = soup.find_all('a')
# print(anchors)


# Print the first paragraph of the HTML Page
# print(soup.find('p'))

# Print the classes of first paragraph of the HTML Page
# print(soup.find('p')['class'])


# Find all the paragraphs(or any element) with class='lead'
# print(soup.find('p',class_='lead'))


# Get the text from tags/soup
# print(soup.find('p').get_text())        # from tag 'p'
# print(soup.get_text())                  # from soup, i.e. it will print text of whole HTML Page (will include the JS code too as text


# Get all the links on the page
# all_links = set()
# for link in anchors:
#     if link.get('href') != '#':
#         linkText = "http://codewithharry.com" + link.get('href')
#         all_links.add(link)
#         print(linkText)


# Comment Example 1
'''
markup = "<p><!-- This is a Comment --></p>"        # Here, there are no spaces between the 'p' and <!--> tags, therefore this is a comment for BeautifulSoup.
soup2 = BeautifulSoup(markup)           # Note: we didn't mentioned 'html.parser' here, so it will automatically use the best available parser for this system, in my case it is 'html5lib
print(soup2.p)                      # <p><!-- This is a Comment --></p>
print(type(soup2.p))                # <class 'bs4.element.Tag'>
print(soup2.p.string)               # Output: This is a Comment
print(type(soup2.p.string))               # Output: <class 'bs4.element.Comment'>                       # This is a Comment Object
'''

'''
# Comment Example 2
markup2 = "<p> <!-- This is a Comment --> </p>"         # Here, spaces are added between the tags, so this is not a comment for BeautifulSoup.
soup3 = BeautifulSoup(markup2)           # Note: we didn't mentioned 'html.parser' here, so it will automatically use the best available parser for this system, in my case it is 'html5lib
print(soup3.p)                      # <p> <!-- This is a Comment --> </p>
print(type(soup3.p))                # <class 'bs4.element.Tag'>
print(soup3.p.string)               # Output: None
print(type(soup3.p.string))               # Output: <class 'NoneType'>                              # This is NOT a Comment Object
'''



# Target an element using 'Id'
navbarSupportedContent = soup.find(id='navbarSupportedContent')
# print(navbarSupportedContent)           # This prints the complete html part within id='navbarSupportedContent' including it.
# print(navbarSupportedContent.children)  # Output: <list_iterator object at 0x000001B7F50FDB48>
# print(navbarSupportedContent.contents)      # This prints all the content of this div in a form of list.

for elem in navbarSupportedContent.contents:
    print(elem)

for elem in navbarSupportedContent.children:
    print(elem)

''' The above two for loops returns the same output i.e. a list of content of div with id='navbarSupportedContent'.'''
'''
.contents - A tag's children are available as a list        (Stored in Memory)                  # Can be accesses directly
.children - A tag's children are available as a generator   (Not Stored in Memory)        # Can be accessed by iterating the list generated
'''
# For Scraping big pages, we should use 'children' because it is fast. And also, 'contents' uses your memory, whereas 'children' do not eats your memory


for item in navbarSupportedContent.strings:
    print(item)                             # Prints all the Strings within tag with id='navbarSupportedContent'

for item in navbarSupportedContent.stripped_strings:            # Removes all the spaces (stripped) and prints all strings in continuous different lines
    print(item)



# Parents and Parents
# print(navbarSupportedContent.parent)            # Prints the html code of the parent tag of element with id='navbarSupportedContent' including it.
# print(navbarSupportedContent.parents)               # Output: <generator object PageElement.parents at 0x000002EF35F98748>      # Therefore, it can be iterated.

for item in navbarSupportedContent.parents:         # Prints parent, then parent of parents, then parent of parent of parent and so on
    print(item.name)
'''Output:
nav
body
html
[document]
'''


# SIBLINGS
'''Note: 'Spaces' and 'newlines' are also considered as siblings'''
print(navbarSupportedContent.previous_sibling)      # Output is blank, because it is a space or newline
print(navbarSupportedContent.previous_sibling.previous_sibling)     # This gives an output.

print(navbarSupportedContent.next_sibling)           # Output is blank, because it is a space or newline
print(navbarSupportedContent.next_sibling.next_sibling)         # Output: None      -      Because there is no next sibling of next sibling of element with id='navbarSupportedContent'

elem = soup.select('#loginModal')           # Prints the list of html code of elements with id='loginModal'
print(elem)

elem = soup.select('.loginModal')
print(elem)                                # Output: []                -      because there is no elemets with class='loginModal'

elem = soup.select('.modal-footer')
print(elem)                                 # This gives an output because an element with class='modal-footer' exists.

