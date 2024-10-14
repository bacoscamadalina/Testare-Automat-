import time

from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    LINK = 'https://formy-project.herokuapp.com/form'
    driver = webdriver.Chrome()
    driver.get(LINK)
    driver.maximize_window()
    time.sleep(2)

    # construiti un selector pentru selectarea datei de azi (CSS-Selenium) - #datepicker/(By.ID,"datepicker")
    driver.find_element(By.CSS_SELECTOR,"#datepicker").click()
    time.sleep(2)
    # elemente_today = driver.find_elements(By.CLASS_NAME,'today day') - filtrare pe mai multe clase nu functioneaza
    elemente_today = driver.find_elements(By.CSS_SELECTOR,'[class="today day"]')
    print(len(elemente_today))
    elemente_today[0].click()
    time.sleep(3)


    # construiti un selector pentru selectarea datei de azi (XPATH)



finally:
    #eliberam driverul
    driver.quit()