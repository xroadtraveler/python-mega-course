import requests
from bs4 import BeautifulSoup
import pandas

r=requests.get("https://pythonizing.github.io/data/real-estate/rock-springs-wy/LCWYROCKSPRINGS/")
c=r.content

soup=BeautifulSoup(c,"html.parser")

all=soup.find_all("div",{"class":"propertyRow"})

# all[0].find("h4",{"class":"propPrice"}).text.replace("\n","").replace(" ","")

l=[]
for item in all:
    d={}
    d["Address"]=item.find_all("span",{"class":"propAddressCollapse"})[0].text
    d["Locality"]=item.find_all("span",{"class":"propAddressCollapse"})[1].text
    d["Price"]=item.find("h4",{"class":"propPrice"}).text.replace("\n","").replace(" ","")
    try:
        d["Beds"]=item.find("span",{"class":"infoBed"}).find("b").text
    except:
        d["Beds"]=None
    
    try:
        d["Area"]=item.find("span",{"class":"infoSqFt"}).find("b").text
    except:
        d["Area"]=None
    
    try:
        d["Full Baths"]=item.find("span",{"class":"infoValueFullBath"}).find("b").text
    except:
        d["Full Baths"]=None
    
    try:
        d["Half Baths"]=item.find("span",{"class":"infoValueHalfBath"}).find("b").text
    except:
        d["Half Baths"]=None
    
    for column_group in item.find_all("div", {"class":"columnGroup"}):
        # print(column_group)
        for feature_group, feature_name in zip(column_group.find_all("span",{"class":"featureGroup"}),column_group.find_all("span",{"class":"featureName"})):
            # print(feature_group.text, feature_name.text)
            if "Lot Size" in feature_group.text:
                d["Lot Size"]=feature_name.text
    l.append(d)

# print(l)
# print(len(l))


df=pandas.DataFrame(l)
#print(df)

df.to_csv("Output.csv")