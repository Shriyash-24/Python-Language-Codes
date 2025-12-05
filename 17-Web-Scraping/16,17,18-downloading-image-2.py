import requests
import re
import os

user = input("Enter the image name: ")

user_agent = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:145.0) Gecko/20100101 Firefox/145.0"
}
url = f"https://www.google.com/search?q={user}"

response = requests.get(url=url, headers=user_agent).text

# Regex..
pattern = "\\[\"https://.*\\.jpg\",[0-9]+,[0-9]+\\]"

images = re.findall(pattern, response)
print(f"Total images: {len(images)}")
no_of_images = int(input("Enter the number of images to download: "))

if images:
    if not os.path.exists(user):
        os.mkdir(user)
        os.chdir(user)
    else:
        os.chdir(user)
    for image in images[:no_of_images]:
        image_url = eval(image)[0]
        response = requests.get(url=image_url).content
        image_name = image_url.split("/")[-1]
        with open(image_name, "wb") as file:
            file.write(response)

        print(response)
