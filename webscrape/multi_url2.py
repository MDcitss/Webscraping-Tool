import requests 
from bs4 import BeautifulSoup
import os

false_urls = 0
# Start in the file where all the info will go
origin = "/Users/maxdi/source/webscraper-inital/allRevs"
# For the compete website scrape between 50,000 and 90,000
for num in range(10,99):
    os.chdir(origin)
    id = "810" + str(num)
    goodStr = ""
    similarStr = ""
    improvedStr = ""
    responseStr = ""
    feelStr = ""
    locationStr = ""
    URL = "https://www.careopinion.org.au/810" + str(num)
    # URL = input("Enter Value:" )
    page = requests.get(URL)
    # Simulating starting from 81,000 so need to add "810"
    
    fullHTML = BeautifulSoup(page.content,"html.parser")


    errors = fullHTML.find_all("div", class_="messages")
    erStr = str(errors)
    if "We couldn't find the story" in erStr:
        false_urls +=1
        continue

    os.mkdir(id)
    os.chdir(id)
    # using class tag -> potentially usefull for tags, but not getting if it is "what was good?", "what was bad?", ect.
    # allTags = fullHTML.find_all("a", class_="inline-block font-c-1 tooltip")
    # for i in allTags:
    #     print(i.text)

    # tag parent divs

    # Getting the actual review
    review = fullHTML.find(id="opinion_body")
    f = open("review"+id, "ab")
    f.write(review.text.encode())
    f.close

    # Getting time of review
    timediv = fullHTML.find("time")
    timeSub = timediv.attrs["datetime"]
    time = open("time"+id, "ab")
    time.write(str(timeSub).encode())
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

    g = open("whatGood"+id, "ab")
    b = open("whatBad"+id, "ab")
    feel = open("howFeel"+id, "ab")

    g.write(goodStr.encode())
    b.write(improvedStr.encode())
    feel.write(feelStr.encode())
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
    similar = open("similar"+id,"ab")
    similar.write(similarStr.encode())
    similar.close()

    # Getting responses
    responseHTML = fullHTML.find_all("blockquote", class_="froala-view")
    for i in responseHTML:
        # print(i.text)
        # response = i.text
        responseStr += i.text

    resp = open("response"+id,"ab")
    resp.write(responseStr.encode())
    resp.close()

    # Getting location
    location = fullHTML.find_all("span", itemtype="http://schema.org/Organization")
    for loc in location:
        locationStr += loc.text
    locations = open("location"+id, "ab")
    locations.write(locationStr.encode())
    locations.close()

print(false_urls)