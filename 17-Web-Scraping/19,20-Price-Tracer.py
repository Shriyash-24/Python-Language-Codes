import requests
from bs4 import BeautifulSoup

class PriceTracer:
    def __init__(self, url):
        self.url = url
        self.user_agent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:145.0) Gecko/20100101 Firefox/145.0"}
        self.response = requests.get(url = self.url, headers = self.user_agent).text
        self.soup = BeautifulSoup(self.response, 'html.parser')

    def product_title(self):
        title = self.soup.find("span", {'id': "productTitle"})
        if title is not None:
            return title.text.strip()
        else:
            return "Tag not found"

    def product_price(self):
        price = self.soup.find("span", {'class': "a-price-whole"})
        if price is not None:
            return price.text
        else:
            return "Tag not found"

device = PriceTracer(url="https://www.amazon.in/Razer-DeathAdder-Gaming-Mouse-Model/dp/B0FGX8N9KP")
print(device.product_title())
print(device.product_price())
