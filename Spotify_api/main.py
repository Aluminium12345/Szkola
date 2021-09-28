from youtubesearchpython import VideosSearch
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.common.by
import csv, time

driver = webdriver.Firefox()
with open("one_more_rep.csv") as csv_file:
    reader = csv.reader(csv_file, delimiter=',')

    for row in reader:
        for i in row:
            videosearch = VideosSearch(i, limit=1).result()
            r = videosearch['result']
            result = r[0]
            resultfin = result['link']

            driver.get('https://320ytmp3.com/en14/')
            element1 = driver.find_element_by_name("url")
            element1.click()
            element1.send_keys(resultfin, Keys.ENTER)
