import time
from bs4 import BeautifulSoup
from selenium import webdriver
from Objects import *
import pandas as pd


driver = webdriver.Firefox()
url = "https://www.google.com/search?client=firefox-b-d&q=naturkundemuseum+leipzig#lrd=0x47a6f82003be7a73:0x3f22dbe589345cb2,1,,,"
driver.get(url)
iframe_list = driver.find_elements_by_tag_name("iframe")
driver.switch_to.frame(iframe_list[0])
ID = "introAgreeButton"
driver.find_element_by_id(ID).click()
driver.switch_to.default_content()

#try to get all class name and then scroll to the last one - this makes the website automatic scrolling and loading some more reviewse
# initialize // can be done way better - ok for start
x_old = 0
all_elements = driver.find_elements_by_class_name("QWOdjf") # get all the like button who can be scraped and save them in list
x_new = len(all_elements)

while x_new < 598:
    if x_new > x_old:
        x_old = len(all_elements)
        print(x_old)
        # wie bekomme ich das dauerhafte scrollen hin gepaart mit abrechen, wenn es keine veränderung mehr kommt / mit manuelle neu ausführen passt das
        all_elements[-1].location_once_scrolled_into_view
        time.sleep(4)
        all_elements = driver.find_elements_by_class_name("QWOdjf")
        x_new = len(all_elements)
        print(x_new)
    else:
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


"""
while x_new < 598:
    if x_new > x_old:
        x_old = len(all_elements) # update x_old
        print(x_old)
        all_elements[-1].location_once_scrolled_into_view # scroll until the last like button is visible
        time.sleep(4)
        all_elements = driver.find_elements_by_class_name("QWOdjf") # get all like buttons again
        x_new = len(all_elements)
        print(x_new)
    else:
        # maybe if clause is not working in some cases - try with name (e.g. when someone does not write a text or send picture)
        x_old = len(all_elements)
        print(x_old)
        all_elements = driver.find_elements_by_class_name("jxjCjc") # get all names as list
        all_elements[-1].location_once_scrolled_into_view # scroll to last name in list until it is visible
        time.sleep(4)
        all_elements = driver.find_elements_by_class_name("jxjCjc")
        x_new = len(all_elements)
        print(x_new)
        if x_new == x_old: #
            break
"""



