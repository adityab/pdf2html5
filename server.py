from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import selenium
import time, sys

browser = webdriver.Firefox() # Get local session of firefox
browser.get("http://localhost/pdf2html5") # Load page
#assert "Yahoo!" in browser.title
#elem = browser.find_element_by_name("p") # Find the query box
#elem.send_keys("seleniumhq" + Keys.RETURN)
time.sleep(0.2) # Let the page load, will be added to the API
try:
   elem =  browser.find_element_by_xpath("//div[contains(@id,'viewer')]")
   #browser.execute_script("getCanvasImage()")
#   outHTML = browser.execute_script("return extract()") 
   maxPage = int(browser.execute_script("return pdfDoc.numPages"))
   outHTML = ""
   #print maxPage
   for i in range(0, maxPage):
    outHTML += browser.execute_script("return extract()")
    browser.execute_script("goNext()")
    #sleep(500)

   fileStart = "<html><body>"
   fileEnd = "</body></html>"

   
   print outHTML.encode("utf8")
except NoSuchElementException:
    assert 0, "can't find seleniumhq"
browser.close()

