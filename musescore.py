from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium import webdriver
import os
import subprocess
 
prox = Proxy()
prox.proxy_type = ProxyType.MANUAL
prox.http_proxy = "http://localhost:8118"
prox.ssl_proxy = "http://localhost:8118"
 
capabilities = webdriver.DesiredCapabilities.CHROME
prox.add_to_capabilities(capabilities)

driver = webdriver.Firefox()
driver.get("http://www.musescore.com")
button = driver.find_element_by_class_name("login")
button.click()
username = driver.find_element_by_id("edit-name")
username.send_keys("carson.taos@gmail.com")
password = driver.find_element_by_id("edit-pass")
password.send_keys("kevin1327")
login = driver.find_element_by_id("edit-submit")
login.click()
for pages in range(10000):
	url = "https://musescore.com/sheetmusic?sort=relevance&instruments=9&parts=1&page=" + str(pages + 104)
	print(pages + 104)
	if pages % 5 == 0:
		subprocess.call("killall -HUP tor", shell = True)
		time.sleep(1)
	for x in range(20):
		driver.get(url)
		#time.sleep(random.random()/2)
		pagelist = driver.find_element_by_xpath("//div[@class='clearfix node--type-scores']/article[" + str(x+1) + "]/h2/a")
		#time.sleep(random.random()/2)
		pagelist.click()
		#time.sleep(1) 	
		download = driver.find_element_by_class_name("js-score-download-status")
		#time.sleep(random.random()/2)
		download.click()
		#time.sleep(3+random.random())
		xml = driver.find_element_by_xpath("//div[@class='download']/h3[3]/a")
		time.sleep(5)
		xml.click()