import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path = 'F:\Python_Django_Training\Web Scraping Projects\selenium\chromedriver_win32\chromedriver.exe')

driver.get('https://www.google.co.in/')
print(driver.title)

time.sleep(3)

driver.get('https://www.youtube.com/')
print(driver.title)

time.sleep(3)

driver.back()
print(driver.title)

time.sleep(3)

driver.forward()
print(driver.title)

time.sleep(3)

driver.close()