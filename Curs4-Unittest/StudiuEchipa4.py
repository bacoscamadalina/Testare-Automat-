'''
URL = 'https://demo.nopcommerce.com/register'

1. Faceti click pe register si fara a completa nimic
2. Faceti click pe register dupa ce ati completat primele doua campuri(gender,firstName)
   Completati urmatorul rand si verificati urm.eroare. Folositi selectori de tip XPATH
3. Completati formularul si validati inregistrarea corecta
'''
import time
import unittest

from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


# Cream o clasa care mosteneste (TestCase din unittest)
class TestForm(unittest.TestCase):
    URL = 'https://demo.nopcommerce.com/register'
    button_register = (By.XPATH, '//button[@id="register-button"]')

    # Form details
    gender = (By.XPATH, '//span[@class="female"]')
    first_name = (By.CSS_SELECTOR, '[id="FirstName"]')
    last_name = (By.XPATH, '//input[@name="LastName"]')
    day = (By.CSS_SELECTOR, '[name="DateOfBirthDay"]')
    month = (By.CSS_SELECTOR, '[name="DateOfBirthMonth"]')
    year = (By.CSS_SELECTOR, '[name="DateOfBirthYear"]')
    email = (By.XPATH, '//input[@id="Email"]')
    company_name = (By.ID, 'Company')
    password = (By.ID, 'Password')
    confirm_password = (By.CSS_SELECTOR, '[name="ConfirmPassword"]')

    # implementam metoda setUp()
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.URL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    # implementam metoda tearDown()
    def tearDown(self):
        self.driver.quit()

    # construim metodele de test_
    # 1.
    def test_formIncomplete(self):
        button = self.driver.find_element(*self.button_register)
        button.click()

        first_name_err = self.driver.find_element(By.CSS_SELECTOR, '[data-valmsg-for="FirstName"]')
        assert 'First name is required.' in first_name_err.text

        last_name_err = self.driver.find_element(By.CSS_SELECTOR, '[data-valmsg-for="LastName"]')
        assert 'Last name is required.' in last_name_err.text

        email_err = self.driver.find_element(By.CSS_SELECTOR, '[data-valmsg-for="Email"]')
        assert 'Email is required.' in email_err.text

        password_err = self.driver.find_element(By.CSS_SELECTOR, '[data-valmsg-for="Password"]')
        assert 'Password is required.' in password_err.text

        conf_password_err = self.driver.find_element(By.CSS_SELECTOR, '[data-valmsg-for="ConfirmPassword"]')
        assert 'Password is required.' in conf_password_err.text

    # 2.
    def test_firsName(self):
        gend = self.driver.find_element(*self.gender)
        gend.click()

        firstname = self.driver.find_element(*self.first_name)
        firstname.send_keys('Madalina')

        button = self.driver.find_element(*self.button_register)
        button.click()

        last_name_err = self.driver.find_element(By.CSS_SELECTOR, '[data-valmsg-for="LastName"]')
        assert 'Last name is required.' in last_name_err.text

        email_err = self.driver.find_element(By.CSS_SELECTOR, '[data-valmsg-for="Email"]')
        assert 'Email is required.' in email_err.text

        password_err = self.driver.find_element(By.CSS_SELECTOR, '[data-valmsg-for="Password"]')
        assert 'Password is required.' in password_err.text

        conf_password_err = self.driver.find_element(By.CSS_SELECTOR, '[data-valmsg-for="ConfirmPassword"]')
        assert 'Password is required.' in conf_password_err.text


    def test_lastName(self):
        gend = self.driver.find_element(*self.gender)
        gend.click()

        lastname = self.driver.find_element(*self.last_name)
        lastname.send_keys('Bacosca')

        button = self.driver.find_element(*self.button_register)
        button.click()

        first_name_err = self.driver.find_element(By.CSS_SELECTOR, '[data-valmsg-for="FirstName"]')
        assert 'First name is required.' in first_name_err.text

        email_err = self.driver.find_element(By.CSS_SELECTOR, '[data-valmsg-for="Email"]')
        assert 'Email is required.' in email_err.text

        password_err = self.driver.find_element(By.CSS_SELECTOR, '[data-valmsg-for="Password"]')
        assert 'Password is required.' in password_err.text

        conf_password_err = self.driver.find_element(By.CSS_SELECTOR, '[data-valmsg-for="ConfirmPassword"]')
        assert 'Password is required.' in conf_password_err.text


    def test_email(self):
        em = self.driver.find_element(*self.email)
        em.send_keys('anaaaaa@yahoo.com')


        daytime = self.driver.find_element(*self.day)
        daytime.click()
        value = self.driver.find_element(By.XPATH, '//select[@name="DateOfBirthDay"]/option[@value=12]')
        value.click()

        monthtime = self.driver.find_element(*self.month)
        monthtime.click()
        val = self.driver.find_element(By.XPATH, '//select[@name="DateOfBirthMonth"]/option[@value=9]')
        val.click()

        yeartime = self.driver.find_element(*self.year)
        yeartime.click()
        vall = self.driver.find_element(By.XPATH, '//option[@value=2023]')
        vall.click()

        button = self.driver.find_element(*self.button_register)
        button.click()

        first_name_err = self.driver.find_element(By.CSS_SELECTOR, '[data-valmsg-for="FirstName"]')
        assert 'First name is required.' in first_name_err.text

        last_name_err = self.driver.find_element(By.CSS_SELECTOR, '[data-valmsg-for="LastName"]')
        assert 'Last name is required.' in last_name_err.text

        password_err = self.driver.find_element(By.CSS_SELECTOR, '[data-valmsg-for="Password"]')
        assert 'Password is required.' in password_err.text

        conf_password_err = self.driver.find_element(By.CSS_SELECTOR, '[data-valmsg-for="ConfirmPassword"]')
        assert 'Password is required.' in conf_password_err.text

    def test_password(self):
        password = self.driver.find_element(*self.password)
        password.send_keys('12345@ab')

        daytime = self.driver.find_element(*self.day)
        daytime.click()
        value = self.driver.find_element(By.XPATH, '//select[@name="DateOfBirthDay"]/option[@value=12]')
        value.click()

        monthtime = self.driver.find_element(*self.month)
        monthtime.click()
        val = self.driver.find_element(By.XPATH, '//select[@name="DateOfBirthMonth"]/option[@value=9]')
        val.click()

        yeartime = self.driver.find_element(*self.year)
        yeartime.click()
        vall = self.driver.find_element(By.XPATH, '//option[@value=2023]')
        vall.click()

        conf_pas = self.driver.find_element(*self.confirm_password)
        conf_pas.send_keys('12345@ab')

        button = self.driver.find_element(*self.button_register)
        button.click()

        first_name_err = self.driver.find_element(By.CSS_SELECTOR, '[data-valmsg-for="FirstName"]')
        assert 'First name is required.' in first_name_err.text

        last_name_err = self.driver.find_element(By.CSS_SELECTOR, '[data-valmsg-for="LastName"]')
        assert 'Last name is required.' in last_name_err.text

        email_err = self.driver.find_element(By.CSS_SELECTOR, '[data-valmsg-for="Email"]')
        assert 'Email is required.' in email_err.text

    #3.
    def test_registerValid(self):
        gend = self.driver.find_element(*self.gender)
        gend.click()

        firstname = self.driver.find_element(*self.first_name)
        firstname.send_keys('Madalina')


        lastname = self.driver.find_element(*self.last_name)
        lastname.send_keys('Bacosca')


        daytime = self.driver.find_element(*self.day)
        daytime.click()
        value = self.driver.find_element(By.XPATH, '//select[@name="DateOfBirthDay"]/option[@value=12]')
        value.click()


        monthtime = self.driver.find_element(*self.month)
        monthtime.click()
        val = self.driver.find_element(By.XPATH, '//select[@name="DateOfBirthMonth"]/option[@value=9]')
        val.click()


        yeartime = self.driver.find_element(*self.year)
        yeartime.click()
        vall = self.driver.find_element(By.XPATH, '//option[@value=2023]')
        vall.click()


        em = self.driver.find_element(*self.email)
        em.send_keys('anaaaa@yahoo.com')


        comp_name = self.driver.find_element(*self.company_name)
        comp_name.send_keys('IT Factory')


        password = self.driver.find_element(*self.password)
        password.send_keys('12345@ab')

        conf_pas = self.driver.find_element(*self.confirm_password)
        conf_pas.send_keys('12345@ab')


        button = self.driver.find_element(*self.button_register)
        button.click()


        success_message = self.driver.find_element(By.CSS_SELECTOR,'[class="result"]')
        assert 'Your registration completed' in success_message.text