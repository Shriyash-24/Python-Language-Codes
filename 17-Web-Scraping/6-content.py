import requests
url = "http://www.google.com"

response = requests.get(url = url)

print(type(response.content)) # <class 'bytes'>
print(response.content) # Give me html..

# You can put image url inside url variable and response.content will give you bytes of image.
pic = response.content
f = open("image-url", 'WD')
f.write(pic)
# This will download the image or video and put it in this directory.
