'''

Ce este un driver? - un software care lucreaza cu un anumit hardware - ne ofera posibilitatea de a interactiona cu o
pagina web
- obiectul browser de la care putem pleca

- aplicatie web - pot sa ma loghez, complexitate mai ridicata
- pagina web - o aplicatie foarte simpla in care pot sa dau click

Selector = se refera la modul in care identificam elemente din HTML si vom iteractionam cu el
Cand construim un selection construim un mod de a actiona cu elementele HTML ale unei pagini WEB


                            LIBRARIA SELENIUM

- ne pune la dispozitie unelte pt a interactiona cu o pagina web, cel mai important este webdriver
- webdriver = o instanta a unui browser  (from selenium import webdriver)
Inainte de a incepe un proiect trebuie sa instalam o instanta de driver
Exemplu de instantiere:
chrome = webdriver.Chrome()
sau
chrome = webdriver.Chrome(executable path=ChromeDriverManage().install())


                            ELEMENTE DE HTML

HTML = Hyper Text Markup Language
     = colectii de info care definesc ceva pe un site

a = ancora = un link care ne duce de la o pagina
div = division = sectiuni in pagina noastra, paragrafe
input = cand dorim sa introducem date


                                 SELECTORI

= stringuri care o sa identifice unul sau mai multe elemente
Tipuri:
- ID
- Class
- Name
- Link Text - un link
- Partial Link Text - textul din link este foarte lung
- XPATH -
- CSS Selector - toate combinatiile de mai sus

SELECTORI ID
- garanteaza unicitatea elementelor pe site
= identificator unic pt un element
- cautare in codul sursa : INSPECT -> CTRL+F

SELECTORI ClassName
- se refera la atributul "class"


'''
