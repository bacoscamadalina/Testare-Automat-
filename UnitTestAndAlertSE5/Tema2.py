'''
# - Test 1: Intrati pe site-ul https://www.elefant.ro/
  - Accept cookies (hint: open in private tab)
# - Test 2: cautati un produs la alegere (carti) si verificati ca s-au returnat cel putin 10 rezultate
([class="product-title"])
# - Test 3: Extrageti din lista produsul cu pretul cel mai mic [class="current-price "]
(puteti sa va folositi de find_elements)
# - Test 4: Extrageti titlul paginii si verificati ca este corect
# - Test 5: Intrati pe site, accesati butonul cont si click pe conectare.
Identificati elementele de tip user si parola si inserati valori incorecte (valori incorecte inseamna oricare valori
care nu sunt recunoscute drept cont valid)
- Dati click pe butonul "conectare" si verificati urmatoarele:
            1. Faptul ca nu s-a facut logarea in cont
            2. Faptul ca se returneaza eroarea corecta
# - Test 6: Stergeti valoarea de pe campul email si introduceti o valoare invalida (adica fara caracterul "@") si
verificati faptul ca butonul "conectare" este dezactivat
'''

import time

import unittest

from  selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestForm2(unittest.TestCase):
    URL = 'https://www.elefant.ro/'
    cookie_button = (By.CSS_SELECTOR, '[id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]')
    search_button = (By.CSS_SELECTOR, '[class="form-control searchTerm js-has-overlay"]')
    title = (By.XPATH, '/html/head/title')
    cont_button = (By.XPATH,
                                   '/html/body/header/div/nav/div/div[4]/div/ul[1]/li[1]/a[1]/div/i[@class="material-icons"][1]')
    email = (By.ID, 'ShopLoginForm_Login')
    password = (By.ID, 'ShopLoginForm_Password')

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.URL)
        self.driver.implicitly_wait(3)
        time.sleep(10)

    def tearDown(self):
        self.driver.quit()

    #1.
    def test_cookies(self):
        self.driver.find_element(*self.cookie_button).click()
        time.sleep(3)

    #2.
    def test_returnedNumber(self):
        self.driver.find_element(*self.cookie_button).click()
        books = self.driver.find_element(*self.search_button)
        books.send_keys('carti')
        books.submit()
        time.sleep(2)
        nr_elements= self.driver.find_elements(By.CSS_SELECTOR, '[class="product-title"]')
        print(len(nr_elements))
        if len(nr_elements) > 10:
            print('Test 2 : Condition fulfilled.')
        else:
            print('Error')

    #3.
    def test_price(self):
        self.driver.find_element(*self.cookie_button).click()
        time.sleep(3)
        books = self.driver.find_element(*self.search_button)
        books.send_keys('carti')
        books.submit()
        current_price = self.driver.find_elements(By.CSS_SELECTOR, '[class="current-price  sale-price"]')
        min_price = float(current_price[0].text.replace("lei", " ").replace(",", ".").strip())
        for price in current_price[1:]:
            pret = float(price.text.replace("lei", " ").replace(",", ".").strip())
            if pret < min_price:
                min_price = pret
        print(f'Test 3 : Cel mai mic pret este: {min_price}')

    #4.
    def test_title(self):
        self.driver.find_element(*self.cookie_button).click()
        time.sleep(3)
        titlu = self.driver.find_element(*self.title)
        text = 'elefant.ro - mallul online al familiei tale! • Branduri de top, preturi excelente • Peste 500.000 de produse pentru tine!'
        if titlu.text in text:
            print(f'Test 4 : Titlul este :{text} ')
        else:
            print('S-a produs o greseala in partea de cautare')

    #5.
    def test_logPage(self):
        self.driver.find_element(*self.cookie_button).click()
        time.sleep(3)

        cont = self.driver.find_element(*self.cont_button)
        cont.click()
        time.sleep(3)

        self.driver.find_element(By.CSS_SELECTOR, '[class="my-account-login btn btn-primary btn-block"]').click()
        time.sleep(2)

        self.driver.find_element(*self.email).send_keys('madalina123@yahoo.com')
        self.driver.find_element(*self.password).send_keys('12345678')
        self.driver.find_element(By.XPATH, '//div/button[@class="btn btn-primary btn-block"]').click()
        time.sleep(4)

        # Verificam daca s-a facut logarea in cont
        print(f'Title: {self.driver.title}, URL : {self.driver.current_url}')

        # Verificam daca s-a afisat eroarea
        eroare = self.driver.find_element(By.CSS_SELECTOR, '[class="alert alert-danger"]')
        mesaj = 'Adresa dumneavoastră de email / Parola este incorectă. Vă rugăm să încercați din nou.'
        if eroare.text in mesaj:
            print('Test 5 : S-a afisat eroarea corecta')
        else:
            print('Ceva nu functioneaza corect')
        self.driver.find_element(*self.email).clear()
        self.driver.find_element(*self.password).clear()

    def test_LogButton(self):
        self.driver.find_element(*self.cookie_button).click()
        time.sleep(3)

        cont = self.driver.find_element(*self.cont_button)
        cont.click()
        time.sleep(3)

        self.driver.find_element(By.CSS_SELECTOR, '[class="my-account-login btn btn-primary btn-block"]').click()
        time.sleep(2)

        self.driver.find_element(*self.email).send_keys('madalina123')
        self.driver.find_element(*self.password).send_keys('12345678')
        button = self.driver.find_element(By.XPATH, '//div/button[@class="btn btn-primary btn-block"]')
        button.click()
        time.sleep(4)

        time.sleep(3)
        if button.is_enabled():
            print('Butonul este activ')
        else:
            print('Test 6 : Butonul este inactiv')

