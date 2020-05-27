import csv
from bs4 import BeautifulSoup
import requests

url="http://www.bestphotographers.co.uk"

list_result=[]

res=requests.get(url)
html_soup=BeautifulSoup(res.text,'html.parser')

list_ul=html_soup.find_all('ul',class_='list-items')

def get_website(link):
    res=requests.get(link)
    html_txt=BeautifulSoup(res.text,'html.parser')
    url_cont=html_txt.find('table',class_='contact-details')
    web_link=url_cont.a['href']
    return web_link

def scr_fun(url,place):
    res=requests.get(url)
    html_txt=BeautifulSoup(res.text,'html.parser')
    head=html_txt.find_all('div',class_='card-header')
    for h in head:
        name=h.a.text
        link=h.a['href']
        link="http://www.bestphotographers.co.uk"+link
        web_link=get_website(link)
        ph_div=h.find('div',class_='navmenu-right')
        phone=ph_div.span.text
        lst=[name,phone,place,web_link]
        list_result.append(lst)

    print(place)

for ul in list_ul:
    lists=ul.find_all('li')
    for li in lists:
        u=li.a['href']
        t=li.a.text
        URL=url+u
        scr_fun(URL,t)
        

#print(list_result)

#File handling
myFile=open('example.csv','w')
writer=csv.writer(myFile)
for s in list_result:
    try:
        writer.writerow(s)
    except:
        print(s)
        continue

print('writing complete')
