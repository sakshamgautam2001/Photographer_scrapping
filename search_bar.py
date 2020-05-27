from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

letters=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

driver = webdriver.Chrome(ChromeDriverManager().install())
url='http://www.bestphotographers.co.uk/sb/photographers'
driver.get(url)
searchbox=driver.find_element_by_class_name('input-search')
searchbox.click()
searchbox.send_keys('X')
time.sleep(2)
html_soup=driver.page_source
driver.close()
soup=BeautifulSoup(html_soup,'html.parser')
auto_sug=soup.find_all('div',class_='autocomplete-suggestion')
for sg in auto_sug:
    print(sg.text)



