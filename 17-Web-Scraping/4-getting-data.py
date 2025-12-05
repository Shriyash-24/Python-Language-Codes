# We have to install pip install requests.
import urllib
import requests

url = "http://www.google.com"
response = requests.get(url = url)
print(response.status_code) # 200
print(response.headers) # We get long dictionary.
