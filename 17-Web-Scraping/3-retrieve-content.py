# urllib is used to work with urls, and request is used to read the urls
import urllib.request, urllib.parse, urllib.error

url = urllib.request.urlopen("http://www.google.com")
for line in url:
    print(line.decode().strip())
