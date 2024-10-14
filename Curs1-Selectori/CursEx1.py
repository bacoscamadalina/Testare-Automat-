import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Crearea obiectului (driverul browser Chrome)
chrome = webdriver.Chrome()  # obiect de tip Chrome -> driver

# Folosim metoda get a driver-ului pt a naviga spre pagina web
chrome.get("https://formy-project.herokuapp.com/form")
# Maximizam fereastra driver-ului
chrome.maximize_window()

# Pentru a face o pauza intentionata in script trebuie sa aplicam un time.sleep, adica asteptam sa se incarce pagina
time.sleep(1)

# Dorim sa localizam elementul HTML in care sa introducem FirstName
'''
Pentru inceput construim un selector:
first_name = chrome.find_element(By.ID,'id="first-name"') -> va produce o eroare deoarece valoarea trebuie sa fie 
doar "first_name"
'''
# Variante:
# first_name = chrome.find_element(By.ID,"first-name")  # tot timpul pornim de la driver
first_name = chrome.find_element(By.CSS_SELECTOR, '[id="first-name"]')

# Introducem o valoare
first_name.send_keys('Ion')  # metoda primeste valori
time.sleep(1)

# Dorim sa localizam elementul HTML in care sa introducem LastName
last_name = chrome.find_element(By.ID, "last-name")
last_name.send_keys('Antoci')
time.sleep(1)

# Completam campul job title folosind un selector CSS_Selector cu filtrare pe atributul place-holder
job_title = chrome.find_element(By.CSS_SELECTOR,'[placeholder="Enter your job title"]')
job_title.send_keys('Sofer')
time.sleep(1)
# Ce tip de date are job_title?
print(type(job_title))
# Printam valoarea atributului class al elementului job_title
print(job_title.get_attribute('class'))

'''
Tema: Completati urmatoarele 2 parti din formular care se refera la HighestLevelofEducation si Sex
'''
# Highest  level of education
chrome.find_element(By.ID,"radio-button-1").click()
time.sleep(1)

# Sex
chrome.find_element(By.ID,"checkbox-1").click()
time.sleep(1)

#Bonus: Years of experience, Date



#Localizati butonul de submit si faceti click
chrome.find_element(By.LINK_TEXT,'Submit').click()
time.sleep(2)


