import requests
# You have to check another url, the content's name, and content and all before posting.
url = "http://127.0.0.1:8000/post/"

payload = {
    'title': "Greetings",
    'content': "Welcome to python."
}
response = requests.post(url = url, data = payload)

print(response.text)