''' Clasa AdaugaCheltuialaPage contine metodele necesare pentru a adauga o cheltuiala in aplicatie.
    Metodele sunt:
    - adauga_cheltuiala
'''

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Locators.locators import LocatoriPaginaSmartCrm
from selenium.webdriver.support import expected_conditions as EC

class AdaugaCheltuialaPage:
    def __init__(self, driver):
        self.driver = driver
        self.time = time

        # Locatori adaugare cheltuiala
        self.apasa_buton_meniu_finante_locator = LocatoriPaginaSmartCrm.BUTON_FINANTE_XPATH
        self.apasa_buton_cheltuieli_locator = LocatoriPaginaSmartCrm.BUTON_MENIU_CHELTUIELI_XPATH
        self.apasa_buton_adaugare_cheltuiala_locator = LocatoriPaginaSmartCrm.BUTON_ADAUGARE_CHELTUIALA_XPATH
        self.camp_nume_articol_cheltuiala_locator = LocatoriPaginaSmartCrm.CAMP_NUME_ARTICOL_CHELTUIALA_ID
        self.camp_pret_cheltuiala_locator = LocatoriPaginaSmartCrm.CAMP_PRET_CHELTUIALA_ID
        self.selector_angajat_locator = LocatoriPaginaSmartCrm.SELECTOR_ANGAJAT_XPATH
        self.selecteaza_angajat_1_locator = LocatoriPaginaSmartCrm.SELECTEAZA_ANGAJAT_1_XPATH
        self.buton_salvare_cheltuiala_locator = LocatoriPaginaSmartCrm.BUTON_SALVARE_CHELTUIALA_XPATH
        self.buton_actiune_cheltuiala_locator = LocatoriPaginaSmartCrm.BUTON_ACTIUNE_CHELTUIALA_XPATH
        self.buton_sterge_cheltuiala_locator = LocatoriPaginaSmartCrm.BUTON_STERGE_CHELTUIALA_XPATH
        self.buton_confirmare_stergere_cheltuiala_locator = LocatoriPaginaSmartCrm.BUTON_CONFIRMARE_STERGERE_CHELTUIALA_XPATH
        self.nume_cheltuiala_locator = LocatoriPaginaSmartCrm.NUME_CHELTUIALA_XPATH

        # self.mesaj_notificari_sistem_locator = LocatoriPaginaSmartCrm.MESAJ_NOTIFICARI_SISTEM_XPATH
        self.mesaj_notificari_sistem_stergere_locator = LocatoriPaginaSmartCrm.MESAJ_NOTIFICARI_SISTEM_STERGERE_XPATH

    def adauga_cheltuiala(self):
        self.driver.find_element(By.XPATH, self.apasa_buton_meniu_finante_locator).click()
        self.time.sleep(2)
        self.driver.find_element(By.XPATH, self.apasa_buton_cheltuieli_locator).click()
        self.time.sleep(2)
        self.driver.find_element(By.XPATH, self.apasa_buton_adaugare_cheltuiala_locator).click()
        self.time.sleep(2)
        self.driver.find_element(By.ID, self.camp_nume_articol_cheltuiala_locator).send_keys("Cheltuiala Test")
        self.time.sleep(2)
        self.driver.find_element(By.ID, self.camp_pret_cheltuiala_locator).send_keys("100")
        self.time.sleep(2)
        self.driver.find_element(By.XPATH, self.selector_angajat_locator).click()
        self.time.sleep(2)
        self.driver.find_element(By.XPATH, self.selecteaza_angajat_1_locator).click()
        self.time.sleep(2)
        self.driver.find_element(By.XPATH, self.buton_salvare_cheltuiala_locator).click()
        # self.time.sleep(2)


    def sterge_cheltuiala(self):
        self.driver.find_element(By.XPATH, self.buton_actiune_cheltuiala_locator).click()
        self.time.sleep(2)
        self.driver.find_element(By.XPATH, self.buton_sterge_cheltuiala_locator).click()
        self.time.sleep(2)
        self.driver.find_element(By.XPATH, self.buton_confirmare_stergere_cheltuiala_locator).click()
        # self.time.sleep(2)