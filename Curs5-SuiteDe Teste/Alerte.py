import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Alert(unittest.TestCase):
    js_alert_loc = (By.CSS_SELECTOR,'button[onclick="jsAlert()"]')
    js_confirm_loc = (By.CSS_SELECTOR,'button[onclick="jsConfirm()"]')
    js_prompt_loc = (By.CSS_SELECTOR,'button[onclick="jsPrompt()"]')
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://the-internet.herokuapp.com/javascript_alerts')
    def tearDown(self):
        self.driver.quit()

    def test_js_alert(self):
        self.driver.find_element(*self.js_alert_loc).click()
        self.driver.switch_to.alert.accept()
        time.sleep(2)

    @unittest.skip
    def test_js_confirm(self):
        self.driver.find_element(*self.js_confirm_loc).click()
        self.driver.switch_to.alert.accept()
        time.sleep(2)

    def test_js_prompt(self):
        self.driver.find_element(*self.js_prompt_loc).click()
        driver_text = 'text'
        self.driver.switch_to.alert.send_keys(driver_text)
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        print("S-a confirmat alerta si s-a inchis!")