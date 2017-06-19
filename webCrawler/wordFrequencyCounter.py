import requests
from bs4 import BeautifulSoup
import operator

url = 'https://thenewboston.com/forum/search_forums.php?s='

def start(webUrl):
    wordList = []           #declare empty list
    source_code = requests.get(webUrl).text     #connect to thr web url, retrieve the source code of web page and convert the same in text format
    soup = BeautifulSoup(source_code, "html.parser")        #convert the source code to beautiful soup object

    for post_text in soup.findAll('p', {'class' : 'no-margin forum-desc'}):     #loop over all <p> tag values
        content = post_text.string      #convert each tage data to string format
        words = content.lower().split()     #split the string into each seperate words

        for each_word in words:             #loop over the words
            each_word = makeItClean(each_word)      #remove unnecessary symbols and clean each words
            if len(each_word) > 0:                  #check for null words
                #print(each_word)
                wordList.append(each_word)          #append the cleaned words into word list
        
    createDictionary(wordList)                      #convert the word list to dictionary




def makeItClean(word):                  #define clean method for cleaning the words
    symbols = "~`!@#$%^&*()_+-=[]{}\\|:\";\',./<>/"         #define all the available symbols
    for i in range(0, len(symbols)):                        #loop over all the symbols
        word = word.replace(symbols[i], "")                 #replce the symbol with '' / null string
    return word                                             #return the final word




def createDictionary(wordList):             #define create dictionary method
    wordCount = {}                          #declare empty dictionary
    for word in wordList:                   #loop over word list
        if word in wordCount:               #check if the word is already available in the dict
            wordCount[word] += 1            #if yes then increase the count
        else:                               #for the first occurance of the word
            wordCount[word] = 1             #add the word to the dictionary
    
    for key, value in sorted(wordCount.items(), key = operator.itemgetter(1)):      #loop over sorted set of dictionary items and sort using value[operator.itemgetter(1)] or key[operator.itemgetter(0)]
        print(key, value)                                                           #print the dictionary items


start(url)                                  #call the base or actual method and execute the program