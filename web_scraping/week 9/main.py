from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.daraz.pk/catalog/?spm=a2a0e.tm80335142.search.d_go&q=bucktes")
time.sleep(6)

soup = BeautifulSoup(driver.page_source, "html.parser")
products = soup.find_all("div", class_="ant-col")
titles = []

for divs in products:
    title = divs.find("div", class_="RfADt")
    titles.append(title)

df = pd.DataFrame(titles, columns=["titles"])
df.to_excel("daraz.xlsx")
