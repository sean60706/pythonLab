#爬html樹狀結構，包刮子代、鄰居、母代

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")

for child in bsObj.find("table", {"id": "giftList"}).children:
    print(child)