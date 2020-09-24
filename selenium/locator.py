import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='F:\Python_Django_Training\Web Scraping Projects\selenium\chromedriver_win32\chromedriver.exe')

driver.get('http://localhost/form/reg.html')

# search_box.clear()    #clear search box


# Locating one-element by different methods:

# print(driver.find_element_by_id('name').text)				# text of tag
# form = driver.find_element_by_id('form')

driver.find_element_by_name('add').send_keys('address')
# 3) driver.find_element_by_xpath('')
# 4) driver.find_element_by_link_text('continue')			#<a href="#">continue</a>
# 5) driver.find_element_by_partial_link_text('cont') 		#<a href="#">continue</a>
# 6) driver.find_element_by_tag_name('p')					#<p class='content'>..</p>
# 7) driver.find_element_by_class_name('content') 			#<p class='content'>..</p> 
# 8) driver.find_element_by_css_selector(p.content) 		#<p class='content'>..</p>


# # Locating multiple-element by different methods:

names = driver.find_elements_by_id('name')

for i in names:
	print(i)


time.sleep(2)
driver.quit()
# 2) driver.find_elements_by_name('')
# 3) driver.find_elements_by_xpath('')
# 4) driver.find_elements_by_link_text('continue')			#<a href="#">continue</a>
# 5) driver.find_elements_by_partial_link_text('cont') 		#<a href="#">continue</a>
# 6) driver.find_elements_by_tag_name('p')					#<p class='content'>..</p>
# 7) driver.find_elements_by_class_name('content') 			#<p class='content'>..</p> 
# 8) driver.find_elements_by_css_selector(p.content) 		#<p class='content'>..</p>
