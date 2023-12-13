''' Acest modul contine metodele pentru alocarea programului de lucru pentru angajati
    Metodele sunt:
    - adauga_program_angajat
    - sterge_program_angajat
'''

import time
from selenium.webdriver.common.by import By
from Locators.locators import LocatoriPaginaSmartCrm


class AlocareProgramPage:
    def __init__(self, driver):
        self.driver = driver
        self.time = time

        # Locatori alocare program
        self.apasa_buton_meniu_hr_locator = LocatoriPaginaSmartCrm.BUTON_MENIU_HR_XPATH
        self.apasa_buton_meniu_alocare_program_locator = LocatoriPaginaSmartCrm.BUTON_MENIU_ALOCARE_PROGRAM_CSS
        self.apasa_prima_zi_luna_locator = LocatoriPaginaSmartCrm.BUTON_PRIMA_ZI_XPATH
        self.apasa_selector_tip_program_locator = LocatoriPaginaSmartCrm.SELECTOR_TIP_PROGGRAM_XPATH
        self.apasa_selector_program_lucru_locator = LocatoriPaginaSmartCrm.SELECTOR_PROGRAM_LUCRU_XPATH
        self.apasa_buton_salvare_program_locator = LocatoriPaginaSmartCrm.BUTON_SALVARE_PROGRAM_XPATH

        self.apasa_buton_prima_zi_alocata_locator = LocatoriPaginaSmartCrm.BUTON_PRIMA_ZI_ALOCATA_XPATH
        self.apasa_buton_sterge_program_locator = LocatoriPaginaSmartCrm.BUTON_STERGE_PROGRAM_XPATH

        self.mesaj_notificari_sistem_locator = LocatoriPaginaSmartCrm.MESAJ_NOTIFICARI_SISTEM_XPATH

    def adauga_program_angajat(self):
        self.driver.find_element(By.XPATH, self.apasa_buton_meniu_hr_locator).click()
        self.time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, self.apasa_buton_meniu_alocare_program_locator).click()
        self.time.sleep(2)
        self.driver.find_element(By.XPATH, self.apasa_prima_zi_luna_locator).click()
        self.time.sleep(2)
        self.driver.find_element(By.XPATH, self.apasa_selector_tip_program_locator).click()
        self.time.sleep(2)
        self.driver.find_element(By.XPATH, self.apasa_selector_program_lucru_locator).click()
        self.time.sleep(2)
        self.driver.find_element(By.XPATH, self.apasa_buton_salvare_program_locator).click()
        self.time.sleep(2)

    def sterge_program_angajat(self):
        self.driver.find_element(By.XPATH, self.apasa_buton_prima_zi_alocata_locator).click()
        self.time.sleep(2)
        self.driver.find_element(By.XPATH, self.apasa_buton_sterge_program_locator).click()
        self.time.sleep(2)

