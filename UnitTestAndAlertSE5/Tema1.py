"""
1.
- Instantiaza un browser de Chrome.
- Acceseaza pagina https://the-internet.herokuapp.com/
- Maximizeaza fereastra

2. Acceseaza link-ul Form Authentication, folosind un selector potrivit.

3. Identifica elementul ce contine textul "Login Page" si verifica, folosind un assert, ca acest element are textul
asteptat

4. Identifica input-urile username si password,introdu valori valide, si da click pe butonul login

5. Verifica, folosind un assert ca ai ajuns pe pagina https://the-internet.herokuapp.com/secure

6. Da click pe butonul logout

7. Introdu un username corect si o parola incorecta.
Identifica mesajul care apare si verifica in cod ca acela este mesajul asteptat

8. Introdu un username corect.
Gaseste elementul cu tag-ul h4.
Ia textul de pe el si fa split dupa spatiu. Considera fiecare cuvant ca o potentiala parola.
Foloseste o structura iterativa prin care sa introduci rand pe rand parolele si sa apesi login
La final, testul trebuie sa printeze fie "Nu am reusit sa gasesc parola", fie "Parola secreta este [parola]"
"""
import time
import unittest
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By




class TestForm1(unittest.TestCase):
    URL = 'https://the-internet.herokuapp.com/'
    URL2 = 'https://the-internet.herokuapp.com/secure'
    username = (By.ID, 'username')
    password = (By.ID, 'password')
    correct_password = 'SuperSecretPassword!'
    correct_username = 'tomsmith'
    auth_button = (By.CSS_SELECTOR, '[class="fa fa-2x fa-sign-in"]')
    logout_button = (By.LINK_TEXT, 'Logout')
    wrong_password = '1234abc'
    wrong_username = 'SuperrPASS!'
    h4element = (By.CSS_SELECTOR, '[class="subheader"]')


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.URL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def tearDown(self):
        self.driver.quit()

    #2,3,4,5
    def test_loginPage(self):
        self.driver.find_element(By.LINK_TEXT, 'Form Authentication').click()
        login_page = self.driver.find_element(By.XPATH, '//h2[text()="Login Page"]')
        expected_text = "Login Page"
        actual_text = login_page.text
        assert actual_text == expected_text, f"The text is not the one expected. Expected text '{expected_text}' aand displayed text '{actual_text}"
        print("Correctly displayed text")
        self.driver.find_element(*self.username).send_keys(self.correct_username)
        self.driver.find_element(*self.password).send_keys(self.correct_password)

        self.driver.find_element(*self.auth_button).click()
        assert self.driver.current_url == self.URL2, 'The page is incorrect'
        print('Link is correct')

    #6.
    def test_logout(self):
        self.driver.find_element(By.LINK_TEXT, 'Form Authentication').click()
        self.driver.find_element(*self.username).send_keys(self.correct_username)
        self.driver.find_element(*self.password).send_keys(self.correct_password)
        self.driver.find_element(*self.auth_button).click()
        self.driver.find_element(*self.logout_button).click()

    #7
    def test_wrongDetails(self):
        self.driver.find_element(By.LINK_TEXT, 'Form Authentication').click()
        self.driver.find_element(*self.username).send_keys(self.wrong_username)
        self.driver.find_element(*self.password).send_keys(self.wrong_password)
        self.driver.find_element(*self.auth_button).click()

        mesaj_eroare = self.driver.find_element(By.CSS_SELECTOR, '[class="flash error"]')
        mesaj_asteptat = 'Your username is invalid!'
        print(mesaj_asteptat)

        assert mesaj_asteptat in mesaj_eroare.text, f" {mesaj_eroare} is not the message we've been waiting for"
        print("The message is the one we've been waiting for")
        time.sleep(2)

    def test_findPassword(self):
        self.driver.find_element(By.LINK_TEXT, 'Form Authentication').click()
        self.driver.find_element(*self.username).send_keys(self.correct_username)

        h4 = self.driver.find_element(*self.h4element)
        words = h4.text.split(' ')
        print(words)

        pass_found = False
        for i in words:
            self.driver.find_element(*self.username).send_keys(self.correct_username)
            self.driver.find_element(*self.password).send_keys(i)
            self.driver.find_element(*self.auth_button).click()
            if i == self.correct_password:
                pass_found = True
                break

        if pass_found:
            print(f'The secret password is {self.correct_password}')
        else:
            print("I couldn't find the password")