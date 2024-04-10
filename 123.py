from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

myurl = "https://buff.163.com/goods/33960"
zapros = requests.get(myurl)


#этофункция парсинга
soup = bs(zapros.text, "html.parser")

#float_ak = soup.find('span', class_='cru-market')   принимает тег и класс и ищет его
 
#for ak in float_ak:
 #   print(ak.tr['class']) по логике в будущем должно так работать чтоб выводить все калаши с этим флотом


