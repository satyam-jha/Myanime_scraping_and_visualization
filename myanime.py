import csv
import requests
from bs4 import BeautifulSoup
#get the html form site 
url ="https://myanimelist.net/anime/season"




    
cnt = 0
#create the file to save data 
filler = open("myanime{}.csv".format(cnt),'w',encoding="utf-8",newline='')

new = open("textmal.text", 'w',encoding="utf-8")
#create a writer for csv
writer = csv.writer(filler)

rows = ["Name","Score"]
#csv headers
writer.writerow(rows)



f = open("myanimelink.csv",'r')


reader = csv.DictReader(f)
gg = []
gg.append(url)

for link in reader:
    
    print(link["Season"] + "\t:\t"  +link["link"])
    
    gg.append(link["link"])

f.close()

myanimelist = list(dict.fromkeys(gg))


#function to get data 
def get_data(html_file):
    """ geting data from myanimelist """
    #parse the html data
    global cnt
    filler = open("myanime{}.csv".format(cnt),'w',encoding="utf-8",newline='')
    writer = csv.writer(filler)
    cnt += 1
    rows = ["Name","Score"]
    #csv headers
    writer.writerow(rows)

    mal = BeautifulSoup(html_file , "html.parser")

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
                
            #new.write(str(n) + ":" + str(s) + "\n")
                
            #new.write("-------------------------------\n")
                
        else:
                
                
            
            writer.writerow([n,s])
                #writing in csv file
            #new.write(str(n) + ":" +str(s) + "\n")
                
            #new.write("-------------------------------\n")

for i in myanimelist:
    try:
        print(i)
        anime0 =  requests.get(i).text
        get_data(anime0)

    except:
        print("fail")



#closeing the file
filler.close()


new.close()