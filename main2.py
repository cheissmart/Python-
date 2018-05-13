from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError

page_num = 1

while True:

    url = "https://tabelog.com/tw/tokyo/rstLst/" + str(page_num) + "/?SrtT=rt"
    print(url)
    try:
        response = urlopen(url)
    except HTTPError:
        print("Finish!!")
        break
    html = BeautifulSoup(response)

    rst_list = html.find_all("li", {"class":"list-rst"})
    for rst in rst_list:
        en_name = rst.find("a").contents[0]
        blog_url = rst.find("a")["href"]
        ja_name = rst.find("small", {"class":"list-rst__name-ja"}).contents[0]
        rating = rst.find("b", {"class":"c-rating__val"}).contents[0]
        print(ja_name, en_name, rating, blog_url)
    page_num += 1