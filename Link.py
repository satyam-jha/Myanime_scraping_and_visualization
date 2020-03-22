

import csv
import requests
from bs4 import BeautifulSoup
#get the html form site 

f = open("myanimelink.csv",'r')


reader = csv.DictReader(f)

anime = requests.get("https://myanimelist.net/anime/season").text



gg = []

#reader.__next__()
for link in reader:
    
    print(link["Season"] + "\t:\t"  +link["link"])
    #print(str(link[0]) + "  :   " + str(link[-1]) )
    
    gg.append(link["link"])

f.close()

def get_url(html_file):

        #get the html form site 
    
    fill = open("myanimelink.csv",'a',encoding="utf-8",newline='')
    writerlink = csv.writer(fill)
    writerlink.writerow(["Season","link"])
    mal = BeautifulSoup(html_file , "html.parser")

    get = []
    gg = mal.find("div" , class_="horiznav_nav")
    lk = gg.find("ul")
    for link in lk.find_all('li'):
        try:
            url = link.a['href']
            season = link.text.strip("\n").strip(" \n")
            #season = url.split("/")[-1]
        #print(link.a['href'])
            #print("===================\n")
            #print(url)
            #print("===================\n")
            get.append(url)
            writerlink.writerow([season ,url] )
        except:
            print("The END")
    fill.close()
    return get

for i in gg:
    print(i)
    anime = requests.get(i).text
    get_url(anime)


