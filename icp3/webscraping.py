import urllib.request
from bs4 import BeautifulSoup
import os
#assigning  link to a variable
myLink = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
#opening the url
getLink=urllib.request.urlopen(myLink)
#converting to html
soup = BeautifulSoup(getLink,  "html.parser")
#printing the header
print(soup.h1.text)

for link in soup.findAll('a'):
    #printslinks with href in anchor tags
    print(link.get('href'))
    # fetched data from the table class as wikitable sortable plainrowheaders
table = soup.find("table", { "class" : "wikitable sortable plainrowheaders" })
#looping all elements in tr tags
for row in table.findAll('tr'):
    for r in row.findAll('td'):

        cells = r.text
        #prints td elements
        print(cells)

elements = row.find('th')
#prints th elements
print(elements.text)