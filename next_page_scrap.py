from bs4 import BeautifulSoup
import mechanize
import requests

def get_website(link):
    res=requests.get(link)
    html_txt=BeautifulSoup(res.text,'html.parser')
    url_cont=html_txt.find('table',class_='contact-details')
    web_link=url_cont.a['href']
    return web_link

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
        pgno=1
        while(True):
            html_soup=BeautifulSoup(html_soup,'html.parser')
            soup=html_soup.find_all('h3',class_='card-heading')
            for sp in soup:
                name=sp.a.text
                link=sp.a['href']
                link="http://www.bestphotographers.co.uk"+link
                try:
                    web_link=get_website(link)
                except:
                    web_link='not found'
                print(name + '       ' + web_link)
            print('Page no. ' + str(pgno))
            print('------------------')

            next_btn=html_soup.find_all('div',class_='navmenu-right')
            try:
                next_url=next_btn[len(next_btn)-1].a['href']
                next_url=url+next_url
                soup_temp=requests.get(next_url)
                html_soup=soup_temp.text
                pgno=pgno+1
            except:
                break

            

        

dic=['Aberaeron, Ceredigion']

place_specific(dic)