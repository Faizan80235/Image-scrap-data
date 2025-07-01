# import requests
# from bs4 import BeautifulSoup
# import os

# # Web page ka URL
# url = "https://www.paklap.pk/apple-products.html"
# page = requests.get(url)
# soup = BeautifulSoup(page.text, "html.parser")

# # Saari images nikaalna
# images = soup.select("img.product-image-photo")

# # Folder banana jahan images save hongi
# if not os.path.exists("images"):
#     os.mkdir("images")

# # Loop chala ke images download karna
# i = 1  # Counter shuru
# for img in images:
#     src = img.get("src")
#     if src:  # Agar image ka link hai
#         data = requests.get(src).content
#         with open(f"images/img{i}.jpg", "wb") as f:
#             f.write(data)
#         print(f"Image {i} saved.")
#         i += 1





















import  requests
from bs4 import BeautifulSoup
import os

url=requests.get("https://www.paklap.pk/apple-products.html")
soup=BeautifulSoup(url.text,"html.parser")
images = soup.select("img.product-image-photo")
i=1
os.makedirs("images", exist_ok=True)
for img in images :
    src=img.get("src")
    if src:
        