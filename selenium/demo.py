import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path = 'F:\Python_Django_Training\Web Scraping Projects\selenium\chromedriver_win32\chromedriver.exe')

driver.get('https://www.google.co.in/')

print(driver.title)		# Title of the page

print(driver.current_url) # Returns the URL of the current page

driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[2]').click()	# Open subpages of current URL


time.sleep(5)
# print(driver.page_source) # Return HTML Code

driver.close()	# Close current  browser

driver.quit()	# Close all the browser


