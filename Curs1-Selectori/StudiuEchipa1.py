import time

from selenium import webdriver
from selenium.webdriver.common.by import By

"""
1.
- Instantiaza un browser de Chrome.
- Acceseaza pagina https://the-internet.herokuapp.com/
- Maximizeaza fereastra
"""

chrome = webdriver.Chrome()
chrome.get('https://the-internet.herokuapp.com/')
chrome.maximize_window()

"""
2. Acceseaza link-ul Form Authentication, folosind un selector potrivit.
"""

chrome.find_element(By.LINK_TEXT, 'Form Authentication').click()
# time.sleep(2)

"""
3. Identifica elementul ce contine textul "Login Page"
si verifica, folosind un assert, ca acest element are textul asteptat
"""
login_page = chrome.find_element(By.XPATH, '//h2[text()="Login Page"]')

expected_text = "Login Page"
actual_text = login_page.text
assert actual_text == expected_text, f"Textul nu este cel asteptat. Text asteptat '{expected_text}' si text afisat '{actual_text}"
print("Text afisat corect")
# time.sleep(1)

"""
4. Identifica input-urile username si password,
introdu valori valide, si da click pe butonul login
"""
username = chrome.find_element(By.ID, 'username')
username.send_keys('tomsmith')

password = chrome.find_element(By.ID, 'password')
password.send_keys('SuperSecretPassword!')

chrome.find_element(By.CSS_SELECTOR, '[class="fa fa-2x fa-sign-in"]').click()
# time.sleep(2)

"""
5. Verifica, folosind un assert ca ai ajuns pe pagina
https://the-internet.herokuapp.com/secure
"""
url = 'https://the-internet.herokuapp.com/secure'

assert chrome.current_url == url, 'Pagina este incorecta'
print('Linkul este cel corect')

"""
6. Da click pe butonul logout
"""
chrome.find_element(By.LINK_TEXT, 'Logout').click()
# time.sleep(2)

"""
7. Introdu un username corect si o parola incorecta.
Identifica mesajul care apare si verifica in cod ca acela este mesajul asteptat.
"""

username = chrome.find_element(By.ID, 'username')
username.send_keys('admin123')

password = chrome.find_element(By.ID, 'password')
password.send_keys('admin1234')

chrome.find_element(By.CSS_SELECTOR, '[class="fa fa-2x fa-sign-in"]').click()
time.sleep(2)

mesaj_eroare = chrome.find_element(By.CSS_SELECTOR, '[class="flash error"]').text.strip(
    chrome.find_element(By.LINK_TEXT, '×').text)
print(mesaj_eroare)
mesaj_asteptat = 'Your username is invalid!'
print(mesaj_asteptat)

assert mesaj_asteptat.split() == mesaj_eroare.split(), f'{mesaj_eroare} nu reprezinta mesajul asteptat'
print('Mesajul este cel asteptat')
time.sleep(2)

'''
varianta 2 


username2 = mozilla.find_element(By.ID, 'username')
username2.send_keys('tomsmith')
time.sleep(4)

password2 = mozilla.find_element(By.ID, 'password')
password2.send_keys('SuperSecretPassword!!')
time.sleep(4)

submit2 = mozilla.find_element(By.CSS_SELECTOR, 'i.fa.fa-2x.fa-sign-in').click()
time.sleep(3)

mesaj_asteptat = "Your password is invalid!"
html_code =
<div data-alert="" id="flash" class="flash error">
            Your password is invalid!
            <a href="#" class="close">×</a>
          </div>
if mesaj_asteptat in html_code:
    print("Mesajul afisat este: Your password is invalid! ")
else:
    print("Mesajul nu a fost gasit")
time.sleep(3)


'''

"""
8. Introdu un username corect.
Gaseste elementul cu tag-ul h4.
Ia textul de pe el si fa split dupa spatiu. Considera fiecare cuvant ca o potentiala parola.
Foloseste o structura iterativa prin care sa introduci rand pe rand parolele si sa apesi login
La final, testul trebuie sa printeze fie "Nu am reusit sa gasesc parola", fie "Parola secreta este [parola]"
"""
username = chrome.find_element(By.ID, 'username')
username.send_keys('tomsmith')

elementulh4 = chrome.find_element(By.CSS_SELECTOR, '[class="subheader"]')
cuvinte = elementulh4.text.split(' ')
print(cuvinte)

parola = "SuperSecretPassword!"
parola_gasita = False
for i in cuvinte:
    chrome.find_element(By.ID, 'username').send_keys('tomsmith')
    password = chrome.find_element(By.ID, 'password')
    password.send_keys(i)
    chrome.find_element(By.CSS_SELECTOR, '[class="fa fa-2x fa-sign-in"]').click()
    if i == parola:
        parola_gasita = True
        break

if parola_gasita:
    print(f'Parola secreta este {parola}')
else:
    print('Nu am reusit sa gasesc parola')
