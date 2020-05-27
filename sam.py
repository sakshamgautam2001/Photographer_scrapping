from bs4 import BeautifulSoup
import requests

def get_website(link):
    res=requests.get(link)
    html_txt=BeautifulSoup(res.text,'html.parser')
    url_cont=html_txt.find('table',class_='contact-details')
    web_link=url_cont.a['href']
    return web_link

print(get_website('http://www.bestphotographers.co.uk/company/bubbles-photography/'))