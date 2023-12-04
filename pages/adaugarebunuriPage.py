import time
from selenium.webdriver.common.by import By
from Locators.locators import LocatoriPaginaSmartCrm


class AdaugaBunuriPage:
    def __init__(self, driver):
        self.driver = driver
        self.time = time

        # Locatori adaugare cheltuiala
        self.apasa_buton_meniu_achiziitii_locator = LocatoriPaginaSmartCrm.BUTON_MENIU_ACHIZITII_BUNURI_XPATH
        self.apasa_buton_adaugare_active_locator = LocatoriPaginaSmartCrm.BUTON_ADAUGARE_ACTIVE_XPATH
        self.camp_denumire_bun_locator = LocatoriPaginaSmartCrm.CAMP_DENUMIRE_BUN_ID
        self.selector_tip_active_locator = LocatoriPaginaSmartCrm.SELECTOR_TIP_ACTIVE_XPATH
        self.selecteaza_tip_active_locator = LocatoriPaginaSmartCrm.SELECTEAZA_TIP_ACTIVE_XPATH
        self.camp_numar_serie_active_locator = LocatoriPaginaSmartCrm.CAMP_NUMAR_SERIE_ACTIVE_ID
        self.buton_salveaza_active_locator = LocatoriPaginaSmartCrm.BUTON_SALVEAZA_ACTIVE_XPATH
        self.buton_actiune_active_bunuri_locator = LocatoriPaginaSmartCrm.BUTON_ACTIUNE_ACTIVE_BUNURI_XPATH
        self.buton_sterge_active_bunuri_locator = LocatoriPaginaSmartCrm.BUTON_STERGE_ACTIVE_BUNURI_XPATH
        self.buton_confirmare_stergere_active_bunuri_locator = LocatoriPaginaSmartCrm.BUTON_CONFIRMARE_STERGERE_ACTIVE_BUNURI_XPATH


    def adauga_active_bunuri(self):
        self.driver.find_element(By.XPATH, self.apasa_buton_meniu_achiziitii_locator).click()
        self.time.sleep(2)
        self.driver.find_element(By.XPATH, self.apasa_buton_adaugare_active_locator).click()
        self.time.sleep(2)
        self.driver.find_element(By.ID, self.camp_denumire_bun_locator).send_keys("Bun Test")
        self.time.sleep(2)
        self.driver.find_element(By.XPATH, self.selector_tip_active_locator).click()
        self.time.sleep(2)
        self.driver.find_element(By.XPATH, self.selecteaza_tip_active_locator).click()
        self.time.sleep(2)
        self.driver.find_element(By.ID, self.camp_numar_serie_active_locator).send_keys("123456789")
        self.time.sleep(2)
        self.driver.find_element(By.XPATH, self.buton_salveaza_active_locator).click()
        self.time.sleep(2)

    def sterge_active_bunuri(self):
        self.driver.find_element(By.XPATH, self.buton_actiune_active_bunuri_locator).click()
        self.time.sleep(2)
        self.driver.find_element(By.XPATH, self.buton_sterge_active_bunuri_locator).click()
        self.time.sleep(2)
        self.driver.find_element(By.XPATH, self.buton_confirmare_stergere_active_bunuri_locator).click()
        self.time.sleep(2)

