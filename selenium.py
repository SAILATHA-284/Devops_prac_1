from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
print("Sample test case started")
driver=webdriver.Edge()
driver.maximize_window()
driver.get("http://www.google.com/")
search_box=driver.find_element("name","q")
search_box.send_keys("Python Selenium")
search_box.send_keys(Keys.RETURN)
time.sleep(3)
driver.quit()
print("Sample test case completed")

