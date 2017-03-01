#抓取網頁，並且可以使用try-except來處理例外情況
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return  None
    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        title = bsObj.body.h1.text
    except AttributeError as e:
        return None
    return title

title = getTitle("https://www.pythonscraping.com/pages/page1.html")
if title == None:
    print("not found")
else:
    print(title)

"""
try:
    html = urlopen("https://www.pythonscraping.com/pages/page1.html")
except HTTPError as e:
    print("error has been occurse")
else:
    bsObj = BeautifulSoup(html.read(), "html.parser")
    print(bsObj.h1)
finally:
    print("gg")
"""

