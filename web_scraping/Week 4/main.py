# import request
import requests
# import beautfful soup
from bs4 import BeautifulSoup
# url import
url=requests.get("https://www.freeimages.com/")
# beautifulsoup use for extractig html 
soup=BeautifulSoup(url.text,"html.parser")
# img tag finded
img_tag_find=soup.find('img')
# img src get
img_tag_src=img_tag_find.get('src')
# print on it console
print("first_img_url:")
print(img_tag_find)
print(img_tag_src)
# filename for svae as a locla
filname="image.png"
# request get for url
response=requests.get(img_tag_src)
# function save a binary like svg
with open(filname, 'wb') as f:
    # binary content image to local file
    f.write(response.content)
