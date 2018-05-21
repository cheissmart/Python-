from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import pandas as pd


def open_ptt_url(url):
    r = Request(url)
    r.add_header("user-agent", "Mozilla/5.0")
    response = urlopen(r)
    htm = BeautifulSoup(response)
    return htm


df = pd.DataFrame(columns=['標題', '網址', '內容'])


u = "https://www.ptt.cc/bbs/movie/index.html"
html = open_ptt_url(u)

posts = html.find_all("div", {"class":"r-ent"})
for post in posts:
    a_area = post.find("div", {"class":"title"}).find("a")
    if a_area:
        post_url = "https://www.ptt.cc" + a_area["href"]
        print(a_area.string, post_url)
        if "公告" in a_area.string:
            continue
        post_html = open_ptt_url(post_url)
        content = post_html.find("div", {"id":"main-content"})

        removes = content.find_all("div", {"class":"article-metaline"})
        for remove in removes:
            remove.extract()
        removes = content.find_all("div", {"class": "article-metaline-right"})
        for remove in removes:
            remove.extract()
        removes = content.find_all("span", {"class": "f2"})
        for remove in removes:
            remove.extract()
        removes = content.find_all("div", {"class": "push"})
        for remove in removes:
            remove.extract()
        revise = content.text.replace('\r', '').replace('\n', '')
        s = pd.Series([a_area.text, post_url, revise], index = ['標題', '網址', '內容'])
        df = df.append(s, ignore_index=True)

df.to_csv("result.csv", encoding='utf-8')
