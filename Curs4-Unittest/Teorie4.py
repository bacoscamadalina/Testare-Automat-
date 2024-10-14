'''
                                   - Libraria Unit Test -



Levels of Testing:
1. unit testing -> test the individual component
2. integration testing -> test integrated component
3. system testing -> test the entire system (flows, testare de la inregistrarea user-ului, la logare, la stergerea acestuia
) (luam functionalitatile din cap la coada si testam tot)
4.  acceptance testing -> test the final system -> aici participa si persoane de business care stiu cum se foloseste
sistemul

Pentru a ne folosi de libraria unit test, formam o clasa care sa mosteneasca din TestCase
Particularitati:
1. metoda setUp() -> contine pasii care dorim sa se execute inainte de a intra in test. (ex: try.. URL)
2. metoda tearDown() -> executa dupa ce se executa oricare dintre testele pe care le avem(ex: ce avem in finally)
3. toate metodale de test trebuie sa aiba preficul test_


                                            Waituri

Randare(rendering) = proces de transformare a codului HTML,CSS,JavaScript intr-o pagina interactiva pe care vizitatorii
site-ului se asteapta sa o vada la interactiunea cu acea pagina
Implicit wait - asteapta numarul definit de secunde inainte sa dea eroare de element not found (chrome.implicitly_wait(6))
Explicit wait - se face la nivel de element (implicit wait are prioritate)(ex: WebDriverWait(driver,timp)...)
EC - exception condition

presence_of_element_located - returns the WebElement once it is located
visibility_of_element_located - returns the WebElement once it is located and visible
element_to_be_clickable - returns the WebElement once it is visible, enabled and interactable



'''