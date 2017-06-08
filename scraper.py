# imports
from bs4 import BeautifulSoup
import requests
import csv
import string
import collections

# Common words that we want to ignore
notWantedWords=["mir","für","bei","vor","bei","im","und","auf","aus"
,"mit","dem","von","über","alle","will","soll",'',"um"]

# this function returns a soup page object
def getPage(url):
    r = requests.get(url)
    data = r.text
    spobj = BeautifulSoup(data, 'html.parser')
    return spobj

# find header in page
def findHeaders(url):
    content = getPage(url).find(id="mitte_uebersicht").find("nav")
    tmp=content.findAll("header")
    return tmp

# split in words and cleans from unwanted common words and punctuation 
def SplitAndClean(inputwords):
    words=[]
    skip=0
    found=0
    for h in inputwords:
        txt=h.string
        #print(txt)
        words=words+[word.strip(string.punctuation) for word in txt.split()]
    #print(words)
    cleaned=[]
    for c in words:
        if c in notWantedWords:
            skip=skip+1
        else:
            found=found+1
            cleaned=cleaned+[c]
    print("Ignored words: "+str(skip))
    print("Real words found: "+str(found))
    return cleaned

# scraper website: heise.de
def main():
    print("START\n")
    cleaned=[]
    for page in range(0,4):
        print("Scapping page n°: "+str(page+1))
        url = "https://www.heise.de/thema/https?seite="+str(page)
    
        tmp=findHeaders(url)
        cleaned+=SplitAndClean(tmp)
        print("DONE !")

    #print(cleaned)
    counter =collections.Counter(cleaned)
    counter=counter.most_common()
    #print(counter)
 

    print("\n\n\nheise.de/thema/https was scraped completely.\n")

    print("===================================================================\nTop 3 words:")
    print(counter[0:3])
           


# main program

if __name__ == '__main__':
    main()