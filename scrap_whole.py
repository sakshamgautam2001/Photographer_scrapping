import csv
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import mechanize

list_result=[]

def get_website(link):
    res=requests.get(link)
    html_txt=BeautifulSoup(res.text,'html.parser')
    url_cont=html_txt.find('table',class_='contact-details')
    web_link=url_cont.a['href']
    return web_link

def suggestions(letter):
    dic=[]
    driver = webdriver.Chrome(ChromeDriverManager().install())
    url='http://www.bestphotographers.co.uk/sb/photographers'
    driver.get(url)
    searchbox=driver.find_element_by_class_name('input-search')
    searchbox.click()
    searchbox.send_keys(letter)
    time.sleep(2)
    html_soup=driver.page_source
    driver.close()
    soup=BeautifulSoup(html_soup,'html.parser')
    auto_sug=soup.find_all('div',class_='autocomplete-suggestion')
    for sg in auto_sug:
        dic.append(sg.text)

    print(dic)
    return dic

def place_specific(dic):
    br=mechanize.Browser()
    br.set_handle_robots(False)
    url='http://www.bestphotographers.co.uk/sb/photographers'
    for place in dic:
        br.open(url)
        br.select_form(nr=0)
        br.form['s_place']=place
        br.form.set_all_readonly(False)
        html_soup=br.submit()

        while(True):
            html_soup=BeautifulSoup(html_soup,'html.parser')
            soup=html_soup.find_all('div',class_='card-header')
            for sp in soup:
                name=sp.a.text
                link=sp.a['href']
                link="http://www.bestphotographers.co.uk"+link
                try:
                    web_link=get_website(link)
                except:
                    web_link=link
                ph_div=sp.find('div',class_='navmenu-right')
                phone=ph_div.span.text
                lst=[name,phone,web_link,place]
                list_result.append(lst)

            next_btn=html_soup.find_all('div',class_='navmenu-right')
            try:
                next_url=next_btn[len(next_btn)-1].a['href']
                next_url=url+next_url
                soup_temp=requests.get(next_url)
                html_soup=soup_temp.text
            except:
                break

            print(place)


#-----------------------Main Program begins from here----------------------

letters=['U', 'V', 'W', 'Y']

for letter in letters:
    dic = suggestions(letter)
    place_specific(dic)

#---------------------------Program ends here------------------------------


#File handling
myFile=open('U-Z.csv','w')
writer=csv.writer(myFile)
for s in list_result:
    try:
        writer.writerow(s)
    except:
        print(s)
        continue

print('writing complete')

        


