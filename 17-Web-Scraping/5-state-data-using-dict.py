import urllib
import requests

url = "http://www.google.com"
user = {
    "User-Agent": "Mozilla/5.0..." # You stated data here.
}

response = requests.get(url = url)
print(response.status_code) # print(response.headers)