from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd

# Set up the WebDriver
driver = webdriver.Chrome()
driver.get("https://books.toscrape.com/catalogue/category/books/classics_6/index.html")
time.sleep(5)

# Parse the HTML
soup = BeautifulSoup(driver.page_source, "html.parser")

# Find all book items
books = soup.select("ol.row li")

# Initialize lists
titles = []
prices = []

# Loop through each book entry
for book in books:
    title = book.h3.a["title"]
    price = book.select_one(".price_color").text

    titles.append(title)
    prices.append(price)

# Create DataFrame
df = pd.DataFrame({
    "Title": titles,
    "Price": prices
})

# Save to Excel
df.to_excel("all_details.xlsx", index=False)

# Close the driver
driver.quit()
