#這邊操作find的部分

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, "html.parser")

#findAll(標籤,狀態,文字,數量,關鍵字,迴圈)，迴圈是bool，預設true，false就只找最上層
nameList = bsObj.findAll("span",{"class":"green"})
for name in nameList:
    print(name.get_text())


someList = bsObj.findAll(text = "the prince")
print(len(someList))