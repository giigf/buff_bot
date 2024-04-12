from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import ClassBot 
import re

o = Options()
o.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=o)
#driver.get('https://buff.163.com/goods/33960#min_paintwear=0.15&max_paintwear=0.18&page_num=1')
time.sleep(15)
page_num = 1
while True:
    
    driver.get(f'https://buff.163.com/goods/33960')

    time.sleep(5)   

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    table = soup.find('table', attrs={'id':'market-selling-list'})

    data = ""
    price_ = ""
    Skin_ = []
    if table.find_all('tr') is not None:
        for row in table.find_all('tr'):
            if row.find('div', class_='wear-value') is not None:
                data = ''.join(re.findall(r'[\d\.-]',row.find('div', class_='wear-value').text))
            if row.find('strong', class_='f_Strong') is not None:
                price_ = ''.join(re.findall(r'[\d\.-]',row.find('strong', class_='f_Strong').text))
                
            Skin_.append(ClassBot.Skin(data, price_)) 
        
        if page_num < 5:
            page_num += 1
        else: 
            page_num = 1
        for data in Skin_:
            data.print_()
    
        
    
       

