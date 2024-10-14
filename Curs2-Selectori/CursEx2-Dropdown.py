import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

try:
    chrome = webdriver.Chrome()
    chrome.get("https://the-internet.herokuapp.com/dropdown")
    #Scop: construim selectori de tip XPATH
    chrome.maximize_window()
    #Construim selector XPATH relativ pentru elementul Select
    select = chrome.find_element(By.XPATH,"//select")
    dropdown = Select(select)
    dropdown.select_by_value("2")
    time.sleep(2)
    dropdown.select_by_value("1")
    time.sleep(2)
finally:

    chrome.quit()

