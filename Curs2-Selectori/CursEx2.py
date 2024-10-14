import time

from selenium import webdriver
from selenium.webdriver.common.by import By


try:
    # construim un driver (chrome)
    chrome = webdriver.Chrome()
    chrome.get("https://formy-project.herokuapp.com/form")
    #Scop: construim selectori de tip XPATH
    chrome.maximize_window()

    # cautam primul element first_name si introducem un nume:
    chrome.find_element(By.XPATH,"//input").send_keys("Andi")

    #Cautam campul Last_name cu filtrare pe atribut
    chrome.find_element(By.XPATH,'//input[@id="last-name"]').send_keys("Radu")

    #Cautam campul job_title folosind un XPATH absolut
    chrome.find_element(By.XPATH,"/html/body/div/form/div/div[3]/input").send_keys("Tester")

    # Alegeti optiunea College
    lista_optiuni_education=chrome.find_elements(By.XPATH,'//input[@type="radio"]')
    for option in lista_optiuni_education:
        if option.get_attribute('id') == 'radio-button-2':
            option.click()

    # Alegeti optiunea female
    chrome.find_element(By.XPATH,'//input[@id="checkbox-2"]').click()

    time.sleep(2)
finally:
    print(f'Eliberam driverul')
    chrome.quit()


