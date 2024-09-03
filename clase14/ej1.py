from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver= webdriver.Chrome()
driver.get("")

web_element.send_keys("Selenium webdrver" + Keys.ENTER)

time.sleep(30)