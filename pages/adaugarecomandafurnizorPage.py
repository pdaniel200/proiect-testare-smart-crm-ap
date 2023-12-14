''' Clasa AdaugaComandaFurnizorPage contine metodele necesare pentru a adauga o comanda furnizor
    in aplicatie.
    Metodele sunt:
    - adauga_comanda_furnizor
'''

import time
from selenium.webdriver.common.by import By
from Locators.locators import LocatoriPaginaSmartCrm


class AdaugaComandaFurnizorPage:
    def __init__(self, driver):
        self.driver = driver
        self.time = time

        # Locatori adaugare comanda furnizor
        self.buton_meniu_achizitii_locator = LocatoriPaginaSmartCrm.BUTON_MENIU_ACHIZITII_XPATH
        self.buton_meniu_comenzi_furnizori_locator = LocatoriPaginaSmartCrm.BUTON_MENIU_COMENZI_FURNIZORI_XPATH
        self.buton_adaugare_comanda_locator = LocatoriPaginaSmartCrm.BUTON_ADAUGARE_COMANDA_XPATH
        self.selector_furnizor_locator = LocatoriPaginaSmartCrm.SELECTOR_FURNIZOR_XPATH
        self.selecteaaza_furnizor_locator = LocatoriPaginaSmartCrm.SELECTEAZA_FURNIZOR_1_XPATH
        self.selector_produs_locator = LocatoriPaginaSmartCrm.SELECTOR_PRODUS_XPATH
        self.selecteaza_serviciu_locator = LocatoriPaginaSmartCrm.SELECTEAZA_SERVICIU_1_XPATH
        self.camp_cantitate_locator = LocatoriPaginaSmartCrm.CAMP_CANTITATE_PRODUS_XPATH
        self.buton_salvare_comanda_locator = LocatoriPaginaSmartCrm.BUTON_SALVARE_COMANDA_XPATH
        self.buton_salvare_si_marcare_trimisa_locator = LocatoriPaginaSmartCrm.BUTON_SALVARE_SI_MARCARE_TRIMISA_XPATH
        self.buton_actiune_comanda_locator = LocatoriPaginaSmartCrm.BUTON_ACTIUNE_COMANDA_XPATH
        self.buton_sterge_comanda_locator = LocatoriPaginaSmartCrm.BUTON_STERGE_COMANDA_XPATH
        self.buton_confirmare_stergere_comanda_locator = LocatoriPaginaSmartCrm.BUTON_CONFIRMARE_STERGERE_COMANDA_XPATH
        self.text_numar_comanda_locator = LocatoriPaginaSmartCrm.TEXT_NUMAR_COMANDA_XPATH


    def adauga_comanda_furnizor(self):
        self.time.sleep(2)
        self.driver.find_element(By.XPATH, self.buton_adaugare_comanda_locator).click()
        self.time.sleep(2)
        self.driver.find_element(By.XPATH, self.selector_furnizor_locator).click()
        self.time.sleep(2)
        self.driver.find_element(By.XPATH, self.selecteaaza_furnizor_locator).click()
        self.time.sleep(2)
        self.driver.find_element(By.XPATH, self.selector_produs_locator).click()
        self.time.sleep(2)
        self.driver.find_element(By.XPATH, self.selecteaza_serviciu_locator).click()
        self.time.sleep(2)
        self.driver.find_element(By.XPATH, self.camp_cantitate_locator).clear()
        self.driver.find_element(By.XPATH, self.camp_cantitate_locator).send_keys("5")
        self.time.sleep(2)
        self.driver.find_element(By.XPATH, self.buton_salvare_comanda_locator).click()
        self.time.sleep(2)
        self.driver.find_element(By.XPATH, self.buton_salvare_si_marcare_trimisa_locator).click()

    def sterge_comanda_furnizor(self):
        self.time.sleep(2)
        self.driver.find_element(By.XPATH, self.buton_actiune_comanda_locator).click()
        self.time.sleep(2)
        self.driver.find_element(By.XPATH, self.buton_sterge_comanda_locator).click()
        self.time.sleep(2)
        self.driver.find_element(By.XPATH, self.buton_confirmare_stergere_comanda_locator).click()
        self.time.sleep(2)
