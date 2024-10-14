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




import unittest
import time

from selenium import webdriver

from selenium.webdriver.common.by import  By


class TestForm3(unittest.TestCase) :
    LINK = "https://orteil.dashnet.org/cookieclicker/"
    consent = (By.CSS_SELECTOR,'[class="fc-button fc-cta-consent fc-primary-button"]')
    got_it = (By.CSS_SELECTOR,'[class="cc_btn cc_btn_accept_all"]')
    eng_leng = (By.ID,'langSelect-EN')
    cookie_button = (By.XPATH, '//button[@id="bigCookie"]')

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.LINK)
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()

    def test_consGet(self):
        self.driver.find_element(*self.consent).click()
        time.sleep(2)
        self.driver.find_element(*self.got_it).click()
        time.sleep(2)

    def test_language(self):
        self.driver.find_element(*self.consent).click()
        time.sleep(2)
        self.driver.find_element(*self.got_it).click()
        time.sleep(2)
        self.driver.find_element(*self.eng_leng).click()
        time.sleep(2)

    #4,5,6,7
    def test_cookieClickNumberUpgradeGold(self):
        self.driver.find_element(*self.consent).click()
        time.sleep(10)
        self.driver.find_element(*self.got_it).click()
        time.sleep(10)
        self.driver.find_element(*self.eng_leng).click()
        time.sleep(15)
        count = 0
        while count < 15:
            self.driver.find_element(*self.cookie_button).click()
            time.sleep(0.5)
            count += 1

        numar_cookie = self.driver.find_element(By.CSS_SELECTOR, '[id="productPrice0"]')
        text = numar_cookie.text
        if text == '15':
            print(f'Am efectuat un numar de 15 apasari ')
        else:
            print(f'Am efectuat {text} apasari')

        self.driver.find_element(By.CSS_SELECTOR, '[id="product0"]').click()

        cookies_necesare = 100

        while True:
            self.driver.find_element(*self.cookie_button).click()
            numar_cookie = int(self.driver.find_element(By.ID, 'cookies').text.split()[0])
            if numar_cookie >= cookies_necesare:
                self.driver.find_element(By.CSS_SELECTOR, '[id="upgrade0"]').click()
                time.sleep(0.1)
                break
            else:
                self.driver.find_element(*self.cookie_button).click()

        cookies_necesare = 500

        while True:
            self.driver.find_element(*self.cookie_button).click()
            time.sleep(0.1)
            numar_cookie = int(self.driver.find_element(By.ID, 'cookies').text.split()[0])
            if numar_cookie >= cookies_necesare:
                self.driver.find_element(By.CSS_SELECTOR, '[id="upgrade0"]').click()
                break
            else:
                self.driver.find_element(*self.cookie_button).click()
                time.sleep(0.1)

        time.sleep(5)
        '''
         while True:
            self.driver.find_element(*self.cookie_button).click()
            time.sleep(0.1)
            golden = self.driver.find_element(By.CSS_SELECTOR, '[id="goldenCookie"]')
            if golden.is_displayed() == True:
                golden.click()
                print('Cookie gasit')
            else:
                continue
        '''



