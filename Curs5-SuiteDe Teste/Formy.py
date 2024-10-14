import time
import unittest

from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


# Vom crea o clasa
class TestLogin(unittest.TestCase):
    URL = 'https://the-internet.herokuapp.com/login'
    user_lock = (By.ID, 'username')
    password = (By.ID, 'password')
    button_log = (By.XPATH, '//button')

    correct_username = 'tomsmith'
    correct_password = 'SuperSecretPassword!'

    wrong_user = 'an42432'
    wrong_pass = 'pass1123'

    # implementam metoda setUp()
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.URL)
        self.driver.maximize_window()
        # folosim un wait implicit
        self.driver.implicitly_wait(5)

    # implementam metoda tearDown()
    def tearDown(self):
        print(f'Eliberam driverul')
        self.driver.quit()

    # implementam metodele de test(test_numetest)
    def test_validLogin(self):
        # localizarea si interactionarea cu elementele
        user = self.driver.find_element(*self.user_lock) # * - folosita pt a despacheta
        user.send_keys(self.wrong_user)
        time.sleep(3)
        user.send_keys(Keys.CONTROL,'a')
        time.sleep(3)
        user.send_keys(Keys.BACKSPACE)
        user.send_keys(self.correct_username)

        self.driver.find_element(*self.password).send_keys(self.correct_password,Keys.ENTER) # dupa parola trimitem tasta ENTER, nu mai trebuie sa apasam butonul de logIn
        #self.driver.find_element(*self.button_log).click()


        # stabilirea conditiilo de succes: instructiunile folosite sunt cele de assert
        # apare mesajul cu verde: You logged into a secure area!
        mesaj_succes = self.driver.find_element(By.CSS_SELECTOR, '[id="flash"]')
        assert 'You logged into a secure area!' in mesaj_succes.text

    # definim urmatoarele 3 metode de test login incorect care sa contina urm. combinatii :
    # user corect, password incorect
    def test_invalidPass(self):
        self.driver.find_element(*self.user_lock).send_keys(self.correct_username)  # * - folosita pt a despacheta
        self.driver.find_element(*self.password).send_keys(self.wrong_pass)
        self.driver.find_element(*self.button_log).click()
        mesaj_succes = self.driver.find_element(By.CSS_SELECTOR, '[id="flash"]')
        assert 'Your password is invalid!' in mesaj_succes.text

    # user incorect, password corect
    def test_invalidUser(self):
        self.driver.find_element(*self.user_lock).send_keys(self.wrong_user)  # * - folosita pt a despacheta
        self.driver.find_element(*self.password).send_keys(self.correct_password)
        self.driver.find_element(*self.button_log).click()
        mesaj_succes = self.driver.find_element(By.CSS_SELECTOR, '[id="flash"]')
        assert 'Your username is invalid!' in mesaj_succes.text

    # user, password incorecte
    def test_invalidPassUser(self):
        self.driver.find_element(*self.user_lock).send_keys(self.wrong_user)  # * - folosita pt a despacheta
        self.driver.find_element(*self.password).send_keys(self.wrong_pass)
        buton = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(self.button_log))
        # presence_of_element_located() - asteapta un singur parametru, adica o tupla, cu perechea de By si valoarea sel
        '''
        presence_of_element_located - returns the WebElement once it is located
        visibility_of_element_located - returns the WebElement once it is located and visible
        element_to_be_clickable - returns the WebElement once it is visible, enabled and interactable
        '''

        buton.click()

        mesaj_succes = self.driver.find_element(By.CSS_SELECTOR, '[id="flash"]')
        assert 'Your username is invalid!' in mesaj_succes.text

