import requests
from bs4 import BeautifulSoup


def Extract(url):
    response = requests.get(url=url).content
    soup = BeautifulSoup(response, 'lxml')
    tag = soup.td  # td is the tag name
    tag = soup.find('td', {'td': "mp-right"})
    h = tag.find_all("h2")
    content = [span.text for span in h]
    print(content)


Extract(url="https://en.wikipedia.org/wiki/Main_Page")