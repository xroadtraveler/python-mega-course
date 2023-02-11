import requests
from bs4 import BeautifulSoup

r=requests.get("https://pythonizing.github.io/data/real-estate/rock-springs-wy/LCWYROCKSPRINGS/")
c=r.content

soup=BeautifulSoup(c,"html.parser")

all=soup.find_all("div",{"class":"propertyRow"})

# all[0].find("h4",{"class":"propPrice"}).text.replace("\n","").replace(" ","")

for item in all:
    print(item.find("h4",{"class":"propPrice"}).text.replace("\n","").replace(" ",""))
    print(item.find_all("span",{"class":"propAddressCollapse"})[0].text)
    print(item.find_all("span",{"class":"propAddressCollapse"})[1].text)
    try:
        print(item.find("span",{"class":"infoBed"}).find("b").text)
    except:
        print(None)
    
    try:
        print(item.find("span",{"class":"infoSqFt"}).find("b").text)
    except:
        print(None)
    
    try:
        print(item.find("span",{"class":"infoValueFullBath"}).find("b").text)
    except:
        print(None)
    
    try:
        print(item.find("span",{"class":"infoValueHalfBath"}).find("b").text)
    except:
        print(None)
    
    print(" ")