import requests 
from bs4 import BeautifulSoup
import os

origin = os.getcwd()
num = 68
os.chdir("/Users/maxdi/source/webscraper-inital/allRevs")
# os.chdir(origin)
os.mkdir(str(num))
os.chdir(str(num))

goodStr = ""
similarStr = ""
improvedStr = ""
responseStr = ""
feelStr = ""
locationStr = ""
URL = "https://www.careopinion.org.au/827" + str(num)
# URL = input("Enter Value:" )
page = requests.get(URL)
id = str(num)
fullHTML = BeautifulSoup(page.content,"html.parser")


errors = fullHTML.find_all("div", class_="messages")
erStr = str(errors)
if "We couldn't find the story" in erStr:
    print("Invalid URL")
    # continue

# using class tag -> potentially usefull for tags, but not getting if it is "what was good?", "what was bad?", ect.
# allTags = fullHTML.find_all("a", class_="inline-block font-c-1 tooltip")
# for i in allTags:
#     print(i.text)

# tag parent divs

# Getting the actual review
review = fullHTML.find(id="opinion_body")
f = open("review"+id, "w+")
f.write(review.text)
f.close

# Getting time of review
timediv = fullHTML.find("time")
timeSub = timediv.attrs["datetime"]
time = open("time"+id, "w+")
time.write(str(timeSub))
time.close()

# get all good,bad,feeling tags
parentDivs = fullHTML.find_all("div", class_="mb-4")
for i in parentDivs:
    checker = str(i.h3)
    tags = i.find_all("a", class_="inline-block font-c-1 tooltip")    

    if "What was good?"  in checker:
        for tag in tags:
            # good.append(tag.text)
            goodStr += tag.text

    
    if "What could be improved?" in checker:
        for tag in tags:
            # improved.append(tag.text)
            improvedStr += tag.text

    if "How did you feel?" in checker:
        for tag in tags:
            # feel.append(tag.text)
            feelStr += tag.text

g = open("whatGood"+id, "w+")
b = open("whatBad"+id, "w+")
feel = open("howFeel"+id, "w+")

g.write(goodStr)
b.write(improvedStr)
feel.write(feelStr)
g.close()
b.close()
feel.close()

# Getting similar tags
moreAbout = fullHTML.find_all("div", class_="other-tags")
for i in moreAbout:
    tags = i.find_all("a", class_="inline-block font-c-1 tooltip")
    for tag in tags:
        # similar.append(tag.text)
        similarStr += tag.text
similar = open("similar"+id,"w+")
similar.write(similarStr)
similar.close()

# Getting responses
responseHTML = fullHTML.find_all("blockquote", class_="froala-view")
for i in responseHTML:
    # print(i.text)
    # response = i.text
    responseStr += i.text

resp = open("response"+id,"w+")
resp.write(responseStr)
resp.close()

# Getting location
location = fullHTML.find_all("span", itemtype="http://schema.org/Organization")
print(location)
for loc in location:
    locationStr += loc.text
locations = open("location"+id, "w+")
locations.write(locationStr)
locations.close()

# for i in good:
#     goodStr += i
# for i in similar:
#     similarStr += i
# print(goodStr)
# print(similarStr)