################################
#                              #
# Download doodles from google #
#                              #
################################

from urllib.request import urlopen
import json

year = input("輸入年份: ")

for mouth in range(1, 13):
    url = "https://www.google.com/doodles/json/" + year + "/" + str(mouth) + "?hl=zh_TW"
    print(url)
    response = urlopen(url)
    doodles = json.load(response)
    for doodle in doodles:
        img_url = "https:" + doodle['url']
        print(img_url)
        response = urlopen(img_url)
        img = response.read()
        file_name = "result/" + img_url.split("/")[-1]
        f = open(file_name, "wb")
        f.write(img)
        f.close()
