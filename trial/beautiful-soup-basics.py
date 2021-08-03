import requests 
from bs4 import BeautifulSoup

URL = "https://www.careopinion.org.au/82747"
page = requests.get(URL)

fullHTML = BeautifulSoup(page.content,"html.parser")

# using id tag -> usefull for the review section
review = fullHTML.find(id="opinion_body")
print(review.text)
# TO DO: make a text file 

# using class tag -> potentially usefull for tags, but not getting if it is "what was good?", "what was bad?", ect.
allTags = fullHTML.find_all("a", class_="inline-block font-c-1 tooltip")
# for i in allTags:
#     print(i.text)

# tag parent divs
parentDivs = fullHTML.find_all("div", class_="mb-4")
timediv = fullHTML.find("time")
timeSub = timediv.attrs["datetime"]
good = []
improved =[]
feel = []
similar = []

for i in parentDivs:
    checker = str(i.h3)
    tags = i.find_all("a", class_="inline-block font-c-1 tooltip")    

    if "What was good?"  in checker:
        for tag in tags:
            good.append(tag.text)

    
    if "What could be improved?" in checker:
        for tag in tags:
            improved.append(tag.text)

    if "How did you feel?" in checker:
        for tag in tags:
            feel.append(tag.text)

moreAbout = fullHTML.find_all("div", class_="other-tags")

for i in moreAbout:
    tags = i.find_all("a", class_="inline-block font-c-1 tooltip")
    for tag in tags:
        similar.append(tag.text)

goodStr = ""
similarStr = ""
for i in good:
    goodStr += i
for i in similar:
    similarStr += i
