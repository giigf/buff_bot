from bs4 import BeautifulSoup
import requests

myurl = "https://buff.163.com/goods/33960"

zapros = requests.get(myurl)
print(zapros.content)