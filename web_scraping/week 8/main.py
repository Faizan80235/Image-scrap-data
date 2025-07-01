import requests
from bs4 import BeautifulSoup
import pandas as pd

url = requests.get("https://books.toscrape.com/catalogue/category/books/music_14/index.html")
soup = BeautifulSoup(url.text, "html.parser")

finds = soup.select_one(".row ol")
# Collect all book titles
titles = []
for h3 in finds.find_all("h3"):
    title = h3.find("a")["title"]
    titles.append(title)

dataframes = pd.DataFrame(titles, columns=["Title"])

dataframes.to_excel("music_detail.xlsx", index=False)
