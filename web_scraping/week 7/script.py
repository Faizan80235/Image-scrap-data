# step1 => import packages
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
# step 2 => get driver
driver=webdriver.Chrome()
# step 3 => get ur;
driver.get("https://openweathermap.org/")
# step 4 => sleep after run
time.sleep(5)
# step 5 => get html source
html=driver.page_source
soup=BeautifulSoup(html , "html.parser")
nav_code=soup.find('ol', class_='row')
print(nav_code)
# step 6 => get css
element=driver.find_element(By.ID ,"nav-website")
line_height = element.value_of_css_property("line-height")
position = element.value_of_css_property("position")
height = element.value_of_css_property("height")
top = element.value_of_css_property("top")
width = element.value_of_css_property("width")
margin = element.value_of_css_property("margin")
background_color = element.value_of_css_property("background-color")
color = element.value_of_css_property("color")
padding = element.value_of_css_property("padding")
z_index = element.value_of_css_property("z-index")
list_style = element.value_of_css_property("list-style")
display = element.value_of_css_property("display")
flex_direction = element.value_of_css_property("flex-direction")
align_items = element.value_of_css_property("align-items")
font_family = element.value_of_css_property("font-family")

# Print results
print("Line Height:", line_height)
print("Position:", position)
print("Height:", height)
print("Top:", top)
print("Width:", width)
print("Margin:", margin)
print("Background Color:", background_color)
print("Text Color:", color)
print("Padding:", padding)
print("Z-Index:", z_index)
print("List Style:", list_style)
print("Display:", display)
print("Flex Direction:", flex_direction)
print("Align Items:", align_items)
print("Font Family:", font_family)


# step 9 => driver quit

driver.quit()
