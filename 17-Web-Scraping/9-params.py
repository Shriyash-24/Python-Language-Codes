# Params means parameters
import requests
url = "http://127.0.0.1:8000/post"
params = {
    "offset": "10"
}
# When I go to next page, offset10 comes up.. I can pass params to get next page data in python

response = requests.get(url, params=params)
print(response.text)
