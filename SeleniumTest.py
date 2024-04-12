from selenium import webdriver
from bs4 import BeautifulSoup
import time
import ClassBot 

driver = webdriver.Firefox()
driver.get('https://buff.163.com/goods/34099')

time.sleep(5)

soup = BeautifulSoup(driver.page_source, 'html.parser')

table = soup.find('table', attrs={'id':'market-selling-list'})

data = ""
price_ = ""
Skin_ = []
for row in table.find_all('tr'):
    if row.find('div', class_='wear-value') is not None:
        data = row.find('div', class_='wear-value').text
    if row.find('strong', class_='f_Strong') is not None:
        price_ = row.find('strong', class_='f_Strong').text
        
    Skin_.append(ClassBot.Skin(data, price_)) 
  
 
# Close the browser
for data in Skin_:
    print(data.float_, " price: ", data.price)

driver.quit()