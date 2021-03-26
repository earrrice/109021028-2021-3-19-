import requests
from bs4 import BeautifulSoup
req=requests.get("http://dns2.asia.edu.tw/~jdwang/PaperList.htm")
req.encoding="big5"

if req.status_code==200:
    print(req.text)
    soup=BeautifulSoup(req.text, "lxml")
    print(soup)
    result=soup.find_all("li")
    fp=open("out1.txt","w",encoding="big5")#big5
    for val in result:
        text1=val.text.replace("\n","")
        text2=text1.replace("  ","")
        print(text2)
        fp.write(text2+"\n")
    fp.close()
else:
    print("no page")
