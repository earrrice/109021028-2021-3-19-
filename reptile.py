import requests
from bs4 import BeautifulSoup
req=requests.get("http://isrc.ccs.asia.edu.tw/www/myjournal/myjournal.htm")
req.encoding="utf8"

if req.status_code==200:
    print(req.text)
    soup=BeautifulSoup(req.text, "lxml")
    print(soup)
    result=soup.find_all("p")
    fp=open("out2.txt","w",encoding="utf8")#big5
    for val in result:
        text1=val.text.replace("\n","")
        text2=text1.replace("  ","")
        print(text2)
        fp.write(text2+"\n")
    fp.close()
else:
    print("no page")
