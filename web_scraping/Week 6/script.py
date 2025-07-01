# step 1 import packages
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# step 2 driver get
driver=webdriver.Chrome()
# step 3 get url
driver.get("https://www.daraz.pk/")
# step 4 sleep
time.sleep(4)
# Step 5 get xpath
search_input=driver.find_element(By.XPATH ,'//*[@id="q"]')
# step 6 send text
search_input.send_keys("braclet")
#  step 7 enter
search_input.send_keys(Keys.RETURN)
# step 8 again sleep
time.sleep(5)
# step 9 driver close
driver.quit()