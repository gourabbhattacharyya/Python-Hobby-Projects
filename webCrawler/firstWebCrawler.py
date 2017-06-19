import requests                             #import request package to connect to a web URL
from bs4 import BeautifulSoup               #import beautiful soup package for crawling through the source code of a web page
import random                               #random package


def forum_spider(max_page):
    page = 1

    while page <= max_page:
        
        name = random.randrange(100, 1000)
        fileName = str(name) + '_' + str(page) + '_webCrawler' + '.txt'
        fw = open(fileName, 'w')                                    #open a new file for writing
        fw.write("------------------------------------------------Begining------------------------------------------------\n")

        url = "https://thenewboston.com/forum/search_forums.php?s=&orderby=popular&page=" + str(page)       #define URL to be hit for web crawling
        soup = getWebDetails(url)           #get the details of a web URL as soup object format

        for link in soup.findAll('a', {'class' : 'title text-semibold'}):       #loop over all the links with tag <a> in the html cocde of web page
            href = link.get('href')                                             #get all the hyperlink details
            title = link.string                                                 #get the titles of all the links
            print(title + ' : ' + href + ' Authors are : ' + getSingleItemData(href) + '\n')
            fw.write(title + ' : ' + href + ' Authors are : ' + getSingleItemData(href) + '\n')     #write into file
        fw.write("------------------------------------------------End------------------------------------------------")
        fw.close()          #close file object
        page += 1           #increase counter


def getWebDetails(webUrl):                      
    source_code = requests.get(webUrl)                      #connect and get the source code of the web page
    plain_text = source_code.text                           #convert the source code as text format
    soup = BeautifulSoup(plain_text, "html.parser")         #convert the text source code as beautiful soup object
    return soup                                             #return soup object



def getSingleItemData(itemUrl):
    soupItems = getWebDetails(itemUrl)                                      #get the details of a web URL as soup object format
    authors = ''

    for item in soupItems.findAll('a', {'class' : 'user-name'}):            #loop over all the links with tag <a> in the html cocde of web page
        #print(str(item.string.encode('utf-8')) + ' , ')
        authors += str(item.string.encode('utf-8'))                         #encode and convert to string the retrieved user-name
        authors += ' , '
    #return authors

    for link in soupItems.findAll('a'):                                     #loop over all the links with tag <a> in the html cocde of web page
        #print(str(item.string.encode('utf-8')) + ' , ')
        href = link.get('href')                                             #get all the hyperlinks
        authors += href
        authors += ' , '
    return authors                                                          #return values

forum_spider(1)                        #call the forum spider function and start the web crawler
