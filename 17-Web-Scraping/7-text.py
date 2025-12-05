import requests
url = "http://www.google.com"

response = requests.get(url = url)
print(response.text) # text returns us data of webpage as string. (HTML)
print(type(response.text)) # <class 'str'>