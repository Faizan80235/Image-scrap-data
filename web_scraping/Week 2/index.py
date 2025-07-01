# request
import requests
# beautifulsoup
from bs4 import BeautifulSoup
# url
url=requests.get("https://webscraper.io/test-sites/e-commerce/allinone")
soup=BeautifulSoup(url.text,"html.parser")


finded=soup.find('div',class_='product-wrapper card-body')

print(finded)