import requests
from bs4 import BeautifulSoup
import csv
import re

def collectFacebookData(countMax):

    count =0
    new_names =[]
    adverts =[]
    imageUrl =[]
    productInfo =[]
    products =[]
    cleanedProducts =[]
    links =[]
    _soup =""
    productInfo =[]
    __links =[]

    __names =[]

    moreDetails =[]
    images =[]

    
    
    groupUrl = {url} #put link to the group  here as string 
    while count<=countMax:
        URL = groupUrl
        r = requests.get(URL)

        soup = BeautifulSoup(r.content,'html5lib')
      
        for a in soup.findAll('a'):
            if(a.text =="Nyaya Izere"):
                href = a.get('href')
                imageUrl.append(href)

               



        

        for o in soup.findAll('a'):
            if(o.text =="Ona Mamwe Mapositi"):
                href= "https://m.facebook.com"+o.get('href')
                groupUrl =href
                print(href)
            
        count+=1

    findIndividualInfo(imageUrl,new_names,adverts,productInfo,__names,images)   

    
    with open('businessNetworkZimbabwe.csv', 'w',encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(zip(__names,productInfo, imageUrl, images))


   
   

    print("Names's length is ",{len(__names)})
    print("Details's length is ",{len(productInfo)})


    print(productInfo)
    print(images)
    print()


def findIndividualInfo(linksContainer,namesContainer,advertsContainer,productInfo,__names,images):
    
    collectNames(linksContainer,__names)
    __collectNames(linksContainer,__names)
    __links = linksContainer
    findDetails(__links,productInfo)
    collectImageUrl(__links,images)
    # collectMoreDetail(__links,moreDetails)



def findDetails(links,productInfo):
      for link in links:
        URL =link   
        r = requests.get(URL)
        indexs =[]
        soup = BeautifulSoup(r.content,'html5lib')
        __productInfo =soup.find('div',attrs ={'class':'bx by'})
       
        
        if __productInfo is None:
            productInfo.append("")
           
        else:
            _spanInfo =__productInfo.find('div',attrs ={'class':'cb'})
            if _spanInfo is None:
                productInfo.append("")
            else:
                detailText = _spanInfo.text
                productDetail = detailText.replace("(Chatengeswa)","")
                productInfo.append(productDetail)


def collectNames(links, names):
    for link in links:
        
        URL =link   
        r = requests.get(URL)
        indexs =[]
        soup = BeautifulSoup(r.content,'html5lib')
        _soup = soup

        nameContainer = soup.find('h3', attrs = {'class':'br bs bt bu'})

        if nameContainer is None:
            names.append("")
        else:
            namesIdentified = nameContainer.find('a')
            if namesIdentified is None:
                names.append("")

            else:
                namesText = namesIdentified.text
                names.append(namesText)
                # print(namesText)



def __collectNames(links,names):
    for name in names:
        if name =="":
            index = names.index(name)
            link = links[index]

            r = requests.get(link)
            soup = BeautifulSoup(r.content,'html5lib')
            _nameInfo =soup.find('h3',attrs ={'class':'br w bs bt'})

            if _nameInfo is None:
                names[index] =""
            else:
                nmDetail = _nameInfo.find('a')
                if nmDetail is None:
                    names[index] =""
                else:
                    names[index] = nmDetail.text
                    # print(names[index])


def collectImageUrl(links,images):
    for link in links:
        
        URL =link   
        r = requests.get(URL)
        indexs =[]
        soup = BeautifulSoup(r.content,'html5lib')
        _soup = soup

        nameContainer = soup.find('img', attrs = {'class':'ck k'})
        # print(nameContainer)
      
        if nameContainer is None:
            images.append("")
        else:
            url = nameContainer.get('src')
            images.append(url)
            print(url)





collectFacebookData(0) #number varies with the number of pages you want to scrape in the fb group




















































