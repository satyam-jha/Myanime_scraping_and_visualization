import csv
import requests
from bs4 import BeautifulSoup
#get the html form site 
anime = requests.get("https://myanimelist.net/anime/season")


mal = BeautifulSoup(anime.text , "html.parser")
    

#create the file to save data 
filler = open("myanime.csv",'w',encoding="utf-8",newline='')

new = open("textmal.text", 'w',encoding="utf-8")
#create a writer for csv
writer = csv.writer(filler)

rows = ["Name","Score"]
#csv headers
writer.writerow(rows)

def get_url(html_file):

        #get the html form site 
    
    fill = open("myanimelink.csv",'w',encoding="utf-8",newline='')
    writerlink = csv.writer(fill)
    writerlink.writerow(["Season","link"])
    mal = BeautifulSoup(html_file.text , "html.parser")

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

#function to get data 
def get_data(html_file):
    """ geting data from myanimelist """
    #parse the html data
    mal = BeautifulSoup(html_file.text , "html.parser")

    #finding name and score of anime 
    winter = mal.find("div",class_ = "js-categories-seasonal")

    who=winter.find_all("div",class_="seasonal-anime js-seasonal-anime")

        #loop for finding the data 
        

    for win in who :
            
        tittle = win.find("div")
            
            
        aniwin = win.find("div",class_="information")
            
        scoreman = aniwin.find("div", class_ = "scormem")
            
        score = scoreman.find("span",class_="score")
            
        ss = score.text.strip(" ")
            
        name = tittle.p.text
            
    
        print("       ")
            
        n = name.strip(" \n")
            
        s = ss.split()[0].strip(" \n")
            
        print(name.strip(" \n"), end= " : ")
            
        print(ss.split()[0])
            
        print("     ")
            #checking if anime is scored yet 
        if s == "N/A":
                #replacing "NA" with something
            writer.writerow([n,"not scored yet"])
                
            new.write(str(n) + ":" + str(s) + "\n")
                
            new.write("-------------------------------\n")
                
        else:
                
                
            
            writer.writerow([n,s])
                #writing in csv file
            new.write(str(n) + ":" +str(s) + "\n")
                
            new.write("-------------------------------\n")




get_url(anime)
#get_data(anime)

#closeing the file
filler.close()


new.close()