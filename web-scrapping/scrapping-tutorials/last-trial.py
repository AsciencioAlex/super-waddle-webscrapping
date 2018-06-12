from urllib import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    response = urlopen("http://www.indeed.com"+articleUrl)
    bsObj = BeautifulSoup(response)
    return bsObj.find("link", {"id":"attribute"}).findAll("a", href=re.compile("^(/jobs/)((?!:).)*$"))

links = getLinks("/jobs/Marijuana")
while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
    print(newArticle)
    links = getLinks(newArticle)