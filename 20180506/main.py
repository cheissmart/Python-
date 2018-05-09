################################
#                              #
# Get FB Fan-pages users like  #
#                              #
################################

from facebook import GraphAPI
from urllib.request import urlopen
import json

token = "EAACEdEose0cBABmtSOWXZASD7QQVZAt4GGBF23XUFxENE98yhLsZANsvOg3iioxoomR8p051nK7BCYBn4XwuSujAGXox59hqYpyC2FiPvXsRppxjUTYHUB5Bd4ZBaQ0x1ZCcGcrojp4kf2dzhSz6IUibgDFJZAkgcm8yTGsNejR0qjdZBpAvX6NLfsg0ajeD07gogBDrHBRDAZDZD"
g = GraphAPI(access_token = token)
ct = 0

pages = g.get_connections("me", "likes")

while True:
    for page in pages["data"]:
        print("%d."%ct, page["name"])
        ct += 1
    try:
        url = pages["paging"]["next"]
        print(url)
        response = urlopen(url)
        pages = json.load(response)
    except KeyError:
        break;
