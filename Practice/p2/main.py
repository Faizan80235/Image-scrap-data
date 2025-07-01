from bs4 import BeautifulSoup
import requests
import pandas as pd

response = requests.get("https://zerolifestyle.co/pages/smart-watches")
soup = BeautifulSoup(response.text, "html.parser")

product_divs = soup.find_all("div", class_="product-list__inner")

srces = []
for div in product_divs:
    img_tags = div.find_all("img")
    for img in img_tags:
        src = img.get("src")
        print(src)  
        srces.append(src)


df = pd.DataFrame(srces, columns=["Image Source"])
df.to_excel("image_sources.xlsx", index=False)

print("Saved to image_sources.xlsx")
