import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path = 'F:\Python_Django_Training\Web Scraping Projects\selenium\chromedriver_win32\chromedriver.exe')

driver.get('https://www.google.co.in')

driver.implicitly_wait(10)
search_box = driver.find_element_by_name('q')
search_btn = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]')



search_box.send_keys("youtube")
search_btn.click()

driver.implicitly_wait(60)

driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div[1]/a').click()
time.sleep(10)
driver.quit()