# Importa din Selenium pentru a verifica starea paginii
from selenium.webdriver.support import expected_conditions as EC

# Importa clasele de baza si locatorii paginii de căutare (SearchPageLocators)
from pages.pagina_de_baza import PaginaDeBaza
from data.locators import LocatoriPaginaCautare


# Definire clasa CautarePagina care moștenește funcționalitatea din clasa de bază PaginaDeBaza
class CautarePagina(PaginaDeBaza):

    def __init__(self, driver, wait):
        self.url = "https://duckduckgo.com/"
        self.locator = LocatoriPaginaCautare
        super().__init__(driver, wait)

    # Navigare catre pagina de cautare
    def mergi_la_cautare_pagina(self):
        self.mergi_la_pagina(self.url)

    # Metoda de verificare a titlului paginii
    def verifica_titlu(self, title):
        self.wait.until(EC.title_contains(title))

    # Metoda pentru a efectua o cautare, introducand un text in câmpul de cautare si apasand butonul de cautare
    def reazizare_cautare(self, input_text):
        self.driver.find_element(*self.locator.SEARCH_INPUT).send_keys(input_text)
        self.driver.find_element(*self.locator.SEARCH_BUTTON).click()
        # asteapta ca rezultatele căutarii sa fie prezente in pagina
        self.wait.until(EC.presence_of_element_located(self.locator.RESULTS))
        # salveaza o captura de ecran a rezultatelor intr-un fișier PNG
        self.driver.save_screenshot("results/results.png")

    ''' def reazizare_login(self, input_text):
        self.driver.find_element(*self.locator.SEARCH_INPUT).send_keys(input_text)
        self.driver.find_element(*self.locator.SEARCH_BUTTON).click()
        # asteapta ca rezultatele căutarii sa fie prezente in pagina
        self.wait.until(EC.presence_of_element_located(self.locator.RESULTS))
        # salveaza o captura de ecran a rezultatelor intr-un fișier PNG
        self.driver.save_screenshot("results/results.png")
'''