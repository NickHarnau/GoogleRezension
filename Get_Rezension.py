import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from  Objects import *
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Firefox()
url = "https://www.google.com/search?client=firefox-b-d&q=naturkundemuseum+leipzig#lrd=0x47a6f82003be7a73:0x3f22dbe589345cb2,1,,,"
driver.get(url)
iframe_list = driver.find_elements_by_tag_name("iframe")
driver.switch_to.frame(iframe_list[0])
ID = "introAgreeButton"
driver.find_element_by_id(ID).click()
driver.switch_to.default_content()

#try to get all class name and then scroll to the last one - this makes the website automatic scrolling and loading some more reviewse
x_new = 0
new_middle = "Start"
while x_new < 598:
    x_old = x_new # wie bekomme ich das dauerhafte scrollen hin gepaart mit abrechen, wenn es keine veränderung mehr kommt / mit manuelle neu ausführen passt das
    all_elements = driver.find_elements_by_class_name("jxjCjc")
    all_elements[-1].location_once_scrolled_into_view
    new_middle = all_elements[-1]
    x_new = len(all_elements)
    if x_new == x_old:
        break







#parse website
response = BeautifulSoup(driver.page_source, 'html.parser')
entry_list = response.find_all("div", attrs={"class":"jxjCjc"})

entries_list = []

for entry in entry_list:
    name = entry.find("class"=="TSUbDb").text
    rating = entry.find("span", attrs={"class":"Fam1ne EBe2gf"})["aria-label"]
    date = entry.find("span", attrs={"class":"dehysf lTi8oc"}).text

    t = entry.find("span", attrs={"class":"review-full-text hide-focus-ring"})
    if t is not None:
        text = t.text
    else:
        text = entry.find("div", attrs={"class":"Jtu6Td"}).text

    lg = entry.find("span", attrs={"class":"QV3IV"})
    if lg is not None:
        local_guide = 1
    else:
        local_guide = 0

    entries_list.append(entries(name, rating, date, text, local_guide))

df_google = pd.DataFrame([vars(f) for f in entries_list])

wait = WebDriverWait(driver,10)
x=0
desiredReviewsCount=30
wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,"jxjCjc")))
while x<desiredReviewsCount:
    driver.find_elements_by_class_name("jxjCjc")
    x = len(driver.find_elements_by_class_name("jxjCjc"))

print(len(driver.find_elements_by_class_name("jxjCjc")))



SCROLL_PAUSE_TIME = 0.5

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height



## next step: scrollen hinbekommen bzw. wie komme ich an alle Kommentare?
#Idee: immer alles in eine Liste packen und dann zum letzten element scrollen

