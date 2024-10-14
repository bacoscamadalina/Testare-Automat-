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

from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    chrome = webdriver.Chrome()
    chrome.get("https://www.elefant.ro/")
    chrome.maximize_window()
    time.sleep(10)
    # Test 1
    cookie = chrome.find_element(By.CSS_SELECTOR, '[id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]')
    cookie.click()
    time.sleep(5)
    # Test 2
    cautare = chrome.find_element(By.CSS_SELECTOR, '[class="form-control searchTerm js-has-overlay"]')
    cautare.send_keys('carti')
    cautare.submit()
    time.sleep(2)
    nr_elemente = chrome.find_elements(By.CSS_SELECTOR, '[class="product-title"]')
    print(len(nr_elemente))
    if len(nr_elemente) > 10:
        print('Test 2 : Conditie indeplinita')
    else:
        print('Eroare')
    # Test 3
    current_price = chrome.find_elements(By.CSS_SELECTOR, '[class="current-price  sale-price"]')
    min_price = float(current_price[0].text.replace("lei", " ").replace(",", ".").strip())
    for price in current_price[1:]:
        pret = float(price.text.replace("lei", " ").replace(",", ".").strip())
        if pret < min_price:
            min_price = pret
    print(f'Test 3 : Cel mai mic pret este: {min_price}')
    # Test 4
    titlu = chrome.find_element(By.XPATH, '/html/head/title').text
    text = 'elefant.ro - mallul online al familiei tale! • Branduri de top, preturi excelente • Peste 500.000 de produse pentru tine!'
    if titlu in text:
        print(f'Test 4 : Titlul este :{text} ')
    else:
        print('S-a produs o greseala in partea de cautare')
    # Test 5
    cont = chrome.find_element(By.XPATH,
                               '/html/body/header/div/nav/div/div[4]/div/ul[1]/li[1]/a[1]/div/i[@class="material-icons"][1]')
    cont.click()
    time.sleep(3)
    chrome.find_element(By.CSS_SELECTOR, '[class="my-account-login btn btn-primary btn-block"]').click()
    time.sleep(2)
    email = chrome.find_element(By.ID, 'ShopLoginForm_Login')
    email.send_keys('madalina123@yahoo.com')
    password = chrome.find_element(By.ID, 'ShopLoginForm_Password')
    password.send_keys('12345678')
    chrome.find_element(By.XPATH, '//div/button[@class="btn btn-primary btn-block"]').click()
    time.sleep(4)

    # Verificam daca s-a facut logarea in cont
    print(f'Titlul paginii redirectionate este: {chrome.title} iar pagina este : {chrome.current_url}')


    # Verificam daca s-a afisat eroarea
    eroare = chrome.find_element(By.CSS_SELECTOR, '[class="alert alert-danger"]')
    mesaj = 'Adresa dumneavoastră de email / Parola este incorectă. Vă rugăm să încercați din nou.'
    if eroare.text in mesaj:
        print('Test 5 : S-a afisat eroarea corecta')
    else:
        print('Ceva nu functioneaza corect')
    email = chrome.find_element(By.ID, 'ShopLoginForm_Login')
    email.clear()
    password = chrome.find_element(By.ID, 'ShopLoginForm_Password')
    password.clear()
    # Test 6
    email = chrome.find_element(By.ID, 'ShopLoginForm_Login')
    email.send_keys('madalina123')
    password = chrome.find_element(By.ID, 'ShopLoginForm_Password')
    password.send_keys('12345678')
    button = chrome.find_element(By.XPATH, '//div/button[@class="btn btn-primary btn-block"]')
    button.click()
    time.sleep(3)
    if button.is_enabled():
        print('Butonul este activ')
    else:
        print('Test 6 : Butonul este inactiv')


finally:
    chrome.quit()
