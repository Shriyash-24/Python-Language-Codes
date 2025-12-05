# pip install bs4 --> Helps us get necessary data
# pip install lxml --> Easy handling of XML, HTML files

import requests
from bs4 import BeautifulSoup

def Extract(url):
    response = requests.get(url=url).content
    soup = BeautifulSoup(response, 'lxml')
    tag = soup.td # td is the tag name
    tag = soup.find('td', {'td':"mp-right"})
    # print(tag) --> L-10
    h = tag.find("h2")
    h = h.find("span") # L-12
    H = tag.find_all("h2") # L-12, we can also use find_all
    print(h) #--> L-11
    

Extract(url = "https://en.wikipedia.org/wiki/Main_Page")
