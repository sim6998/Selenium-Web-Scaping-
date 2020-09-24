import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path='F:\Python_Django_Training\Web Scraping Projects\selenium\chromedriver_win32\chromedriver.exe')

driver.get('http://localhost/form/reg.html')

actions = ActionChains(driver)


address_box = driver.find_element_by_name('add')
address_box.send_keys('Address')
submit = driver.find_element_by_name('submit')

time.sleep(5)

actions.move_to_element(address_box).move_to_element(submit).click(submit)
actions.perform()