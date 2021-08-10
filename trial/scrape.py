from bs4 import BeautifulSoup
import requests
import csv


#with open('Shaun.html') as html_file:
 #   soup = BeautifulSoup(html_file, 'lxml')

#print(soup.prettify())

#match = soup.title.text   #clean text without the tags

""" finds a specific div in a certain class """
""" '.find' will find the first use of the class """
#match = soup.find('div', class_='article') 
#print(match.text) #adding .text will remove any tags and just print the text

""" find_all items in a cetain class """

""" for article in soup.find_all('div', class_="article"):
    headline = article.text
    #print(headline)

    summary = article.p.text
    print(summary) """

""" webscraping from a live website (care opinion Australia) """
source = requests.get('https://www.careopinion.org.au/').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('22717075_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['featured', 'featuredtext'])

#print(soup.prettify())

""" the below will print out the entire blocktag and whatever is within """
featured0 = soup.find('blockquote')

#print(featured0)

print()

""" the below will only print the text within the <anchor> tag (parent tags) """
featured = soup.find('blockquote').a.text

print(featured)

""" will isolate every tag/data inside the pages body tag """
body1 = soup.find('body')

#print(body1)

""" following code will locate and isolate all data that is within a anchor tag and has the class 'font-c-1' """
featuredtext = body1.find('a', class_='font-c-1')

print(featuredtext.text)

""" to avoid missing data breaking the program """
#try:
 #   'some sort of function'
#except expression as identifier:
 #   pass or 'variable = None'


"""  saving the scraped data to a csv file """

csv_writer.writerow([featured, featuredtext])

csv_file.close()