import requests
from bs4 import BeautifulSoup
url=requests.get("https://www.freeimages.com/collection/artificial-intelligence")
soup=BeautifulSoup(url.text,"html.parser")
img_tag=soup.find('img')
img_src=img_tag.get('src')
filenames="imge.svg"
with open (filenames,"wb") as f:
    f.write(response.)
print(url)