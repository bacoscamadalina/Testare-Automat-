'''
# 1. Scrieți un script Python pentru a deschide pagina web a jocului Cookie Clicker folosind Selenium
: https://orteil.dashnet.org/cookieclicker/

# 2. Apasati butonul de Consent si butonul Got it! pentru acceptarea cookie-urilor.

# 3. Selectati limba Engleza

# 4. Utilizați Selenium pentru a localiza elementul cookie pe pagina web și faceți clic pe el programatic.
# Puteți face acest lucru într-un ciclu repetitiv pentru a simula 15 clicuri la fiecare 0,5 secunde

# 5. Obțineți numărul de cookie-uri pe care le-ați câștigat în joc folosind Selenium si verificati ca obtinut 15.

# 6. Localizați elementele de upgrade și simulați clicuri pentru a le achiziționa.

# 7. Detectați și faceți clic pe cookie-urile aurii atunci când apar pe ecran.

# 8. Dezvoltați o strategie pentru achiziționarea eficientă a upgrade-urilor.

'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


try:
    #1.
    LINK = 'https://orteil.dashnet.org/cookieclicker/'
    driver = webdriver.Chrome()
    driver.get(LINK)
    driver.maximize_window()
    time.sleep(3)

    #2.
    driver.find_element(By.CSS_SELECTOR,'[class="fc-button fc-cta-consent fc-primary-button"]').click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR,'[class="cc_btn cc_btn_accept_all"]').click()
    time.sleep(2)

    #3.
    driver.find_element(By.ID,'langSelect-EN').click()
    time.sleep(15)

    #4.
    count = 0
    while count < 15:
        driver.find_element(By.XPATH,'//button[@id="bigCookie"]').click()
        time.sleep(0.5)
        count+=1

    #5.
    numar_cookie = driver.find_element(By.CSS_SELECTOR,'[id="productPrice0"]')
    text = numar_cookie.text
    if text == '15' :
        print(f'Am efectuat un numar de 15 apasari ')
    else:
        print(f'Am efectuat {text} apasari')

    driver.find_element(By.CSS_SELECTOR,'[id="product0"]').click()


    #6.
    cookies_necesare = 100

    while True:
        driver.find_element(By.XPATH, '//button[@id="bigCookie"]').click()
        numar_cookie = int(driver.find_element(By.ID, 'cookies').text.split()[0])
        if numar_cookie >= cookies_necesare:
            driver.find_element(By.CSS_SELECTOR,'[id="upgrade0"]').click()
            time.sleep(0.1)
            break
        else:
            driver.find_element(By.XPATH, '//button[@id="bigCookie"]').click()

    cookies_necesare = 500

    while True:
        driver.find_element(By.XPATH, '//button[@id="bigCookie"]').click()
        time.sleep(0.1)
        numar_cookie = int(driver.find_element(By.ID, 'cookies').text.split()[0])
        if numar_cookie >= cookies_necesare:
            driver.find_element(By.CSS_SELECTOR, '[id="upgrade0"]').click()
            break
        else:
            driver.find_element(By.XPATH, '//button[@id="bigCookie"]').click()
            time.sleep(0.1)

    time.sleep(5)
    '''
     #7.
         while True:
        driver.find_element(By.XPATH, '//button[@id="bigCookie"]').click()
        time.sleep(0.1)
        golden = driver.find_element(By.CSS_SELECTOR,'[id="goldenCookie"]')
        if golden.is_displayed() == True:
            golden.click()
            print('Cookie gasit')
        else:
            continue

    '''







finally:
    driver.quit()