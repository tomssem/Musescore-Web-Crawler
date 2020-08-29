from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium import webdriver
import os
import subprocess

def find_button_with_span(driver, text):
    all_buttons = driver.find_elements_by_xpath("//button")
    for b in all_buttons:
        spans = b.find_elements_by_xpath("span")
        if len(spans) > 0:
            assert(len(spans) == 1)
            print(spans[0].text)
            if spans[0].text == text:
                return b

def find_button_with_class(driver, class_text):
    all_buttons = driver.find_elements_by_xpath("//button")
    for b in all_buttons:
        if not len(b.text):
            if b.get_attribute("class") == class_text:
                return b
 
prox = Proxy()
prox.proxy_type = ProxyType.MANUAL
prox.http_proxy = "http://localhost:8118"
prox.ssl_proxy = "http://localhost:8118"

capabilities = webdriver.DesiredCapabilities.CHROME
prox.add_to_capabilities(capabilities)

fp = webdriver.FirefoxProfile()
fp.set_preference("browser.download.folderList",2)
fp.set_preference("browser.download.manager.showWhenStarting",False)
fp.set_preference("browser.download.dir", os.getcwd())
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/zip")

driver = webdriver.Firefox(firefox_profile=fp)
driver.get("http://www.musescore.com")
print("Login")
input("")
for pages in range(10000):
    url = "https://musescore.com/sheetmusic?sort=relevance&instruments=9&parts=1&page=" + str(pages + 104)
    print(pages + 104)
    if pages % 5 == 0:
        subprocess.call("killall -HUP tor", shell=True)
        time.sleep(1)
    for x in range(20):
        driver.get(url)
        # time.sleep(random.random()/2)
        # images = driver.find_element_by_xpath("//a[contains(@src, 'scoredata')]")
        results = driver.find_elements_by_class_name('SA76l')
        # time.sleep(random.random()/2)
        # pagelist = driver.find_element_by_xpath("//img[contains(@src, 'scoredata')]")
        print(results)
        for i, result in enumerate(results):
            print(1)
            result.click()
            try:
                download_button = find_button_with_span(driver, "Download")
                download_button.click()
                musicxml_button = find_button_with_span(driver, "MusicXML")
                musicxml_button.click()
                close_button = find_button_with_class(driver, "_2Ifc- _8pMIq _3qfU_ _2uj9v _1Us9e _3HJAX _8B-BO _15kzJ")
                close_button.click()
            except Exception:
                print("Error")
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


        # <img src="https://musescore.com/static/musescore/scoredata/gen/6/7/2/6314276/5c33187ef956c5f222dcbff0dcd539a7247698c3/score_0.png@203x287?no-cache=1598515209&amp;bgclr=ffffff" alt="Song 3 + 4 -( 5 x 7) sheet music arranged by creatively names songs  for Mixed Trio" class="_1QTgP _3czii">
        # https://musescore.com/user/69096/scores/5913469

        # <button type="button" class="_3L7Ul _3qfU_ _38TLP _3A7i9 _2XPrY _13O-4 _15kzJ"><svg viewBox="0 0 24 24" class="mU4Rd jlFC3 fHHDK _20alw D0Tij"><path d="M9.6 2.4h4.8V12h2.784l-5.18 5.18L6.823 12H9.6V2.4zM19.2 19.2H4.8v2.4h14.4v-2.4z" fill="#fff"></path></svg><span class="_3R0py">Download</span></button>
