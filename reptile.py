import requests
from bs4 import BeautifulSoup
req=requests.get("http://210.70.80.21/-bs109021028/a.html")
req.encoding="utf8"
soup=BeautifulSoup(req.text)

if req.status_code==200:
    #print(req.text)
    result=soup.find_all("li")
    print(result)
else:
    print("no page")
print(req.status_code)