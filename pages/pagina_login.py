# Importa din Selenium pentru a verifica starea paginii
import time

from selenium.webdriver.support import expected_conditions as EC

# Importa clasele de baza si locatorii paginii de căutare (SearchPageLocators)
from pages.pagina_de_baza import PaginaDeBaza
from data.locators import LocatoriPaginaSmartCrm


# Definire clasa CautarePagina care moștenește funcționalitatea din clasa de bază PaginaDeBaza
class DeschidePagina(PaginaDeBaza):

    def __init__(self, driver, wait):
        self.adresa_smart_crm = "https://smart-crm.ro/"
        self.locator = LocatoriPaginaSmartCrm
        super().__init__(driver, wait)

    # Navigare catre pagina de cautare
    def mergi_la_pagina_scrm(self):
        self.mergi_la_pagina(self.adresa_smart_crm)

    # Metoda de verificare a titlului paginii
    def verifica_titlu(self, title):
        self.wait.until(EC.title_contains(title))

    def realizare_login(self, input_text):
        time.sleep(2)
        # salveaza o captura de ecran a rezultatelor intr-un fișier PNG
        self.driver.save_screenshot("results/main_page.png")
        self.driver.find_element(*self.locator.BUTON_AUTENTIFICARE).click()
        time.sleep(2)
        self.driver.find_element(*self.locator.USERNAME_INPUT).send_keys('testcompany@smart-crm.ro')
        time.sleep(1)
        self.driver.find_element(*self.locator.BUTON_INAINTE).click()
        # asteapta pana campul parola sa fie prezente in pagina
        time.sleep(3)
        self.driver.find_element(*self.locator.PASSWORD_INPUT).send_keys('cGR4n93O9N9Nel9a')
        self.driver.find_element(*self.locator.BUTON_LOGIN).click()
        time.sleep(3)
        # salveaza o captura de ecran a rezultatelor intr-un fișier PNG
        self.driver.save_screenshot("results/login_page.png")
        self.driver.get("https://app.smart-crm.ro/public/account/tasks")
        time.sleep(3)
        self.driver.find_element(*self.locator.PORNIRE_CRONOMETRU).click()
        time.sleep(10)
        self.driver.find_element(*self.locator.OPRIRE_CRONOMETRU).click()
        # salveaza o captura de ecran a rezultatelor intr-un fișier PNG
        self.driver.save_screenshot("results/task_started.png")
        time.sleep(5)
        self.driver.find_element(*self.locator.BUTON_LOGOUT).click()
        time.sleep(3)
