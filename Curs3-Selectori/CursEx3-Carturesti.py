import time

from selenium import webdriver

from selenium.webdriver.common.by import  By


try:
    LINK = "https://carturesti.ro/"
    driver = webdriver.Chrome()
    driver.get(LINK)
    driver.maximize_window()
    time.sleep(3)

    #acceptam modulele de cookie
    driver.find_element(By.CSS_SELECTOR,'[class="cc-btn cc-allow"]').click()
    time.sleep(2)

    # deschidem meniul de produse, selector de tip xpath
    driver.find_element(By.XPATH,'//button/span/span').click()

    # deschidem meniul de login, selector XPATH - click-am elementul vizibil - pozitia 1
    list_login=driver.find_elements(By.XPATH,"//button/span[contains(text(),'Login')]")
    print(len(list_login))
    list_login[1].click()
    time.sleep(4)

    #facem click pe butonul utilizator existent pentru a face login
    driver.find_element(By.XPATH,'//button[@data-target="modalLoginForm"]').click()
    time.sleep(3)


    # completam campul username
    username = driver.find_element(By.XPATH,'//*[@name="LoginForm[email]"]')
    username.send_keys('ana123@yahoo.com')

    # completam campul password
    password = driver.find_element(By.XPATH,'//input[@type="password"]')
    password.send_keys('parola123@')

    #facem click pe autentificare
    driver.find_element(By.XPATH,'//button[@name="login-button"]').click()
    time.sleep(2)

    #verificati faptul ca am ajuns pe o pagina noua: https://carturesti.ro/site/login
    current_title = driver.title
    current_url = driver.current_url
    print(f'Te afli pe pagina: {current_url} si titlul este: {current_title}')
    assert "Autentificare" == current_title
    assert "https://carturesti.ro/site/login" == current_url
    print('Asserts ok')

finally:
    driver.quit()