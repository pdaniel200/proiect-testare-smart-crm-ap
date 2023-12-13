''' Pagina conturi bancare transfer
    Metodele sunt:
    - transfera_intre_conturi
'''

import time
from selenium.webdriver.common.by import By
from Locators.locators import LocatoriPaginaSmartCrm


class ConturiBancareTransferPage:
    def __init__(self, driver):
        self.driver = driver
        self.time = time

        # Locatori transfer cont bancar
        self.apasa_nume_detinator_cont_locator = LocatoriPaginaSmartCrm.NUME_DETINATOR_CONT_XPATH
        self.apasa_buton_transfer_bancar_locator = LocatoriPaginaSmartCrm.BUTON_TRANSFER_CSS
        self.apasa_selector_in_contul_locator = LocatoriPaginaSmartCrm.SELECTOR_IN_CONTUL_XPATH
        self.apasa_cont2companie2_locator = LocatoriPaginaSmartCrm.SELECTOR_CONT2COMPANIE_XPATH
        self.camp_cantitate_locator = LocatoriPaginaSmartCrm.CAMP_CANTITATE_ID
        self.apasa_buton_salvare_locator = LocatoriPaginaSmartCrm.BUTON_SALVARE_XPATH
        self.text_nume_detinator_cont1_locator = LocatoriPaginaSmartCrm.TEXT_NUME_DETINATOR_CONT1_XPATH
        self.sold_cont_bancar_locator = LocatoriPaginaSmartCrm.SOLD_CONT_BANCAR_XPATH

    def transfera_intre_conturi(self):
        self.driver.find_element(By.CSS_SELECTOR, self.apasa_buton_transfer_bancar_locator).click()
        self.time.sleep(2)
        self.driver.find_element(By.XPATH, self.apasa_selector_in_contul_locator).click()
        self.time.sleep(2)
        self.driver.find_element(By.XPATH, self.apasa_cont2companie2_locator).click()
        self.time.sleep(2)
        self.driver.find_element(By.ID, self.camp_cantitate_locator).send_keys("10")
        self.time.sleep(2)
        self.driver.find_element(By.XPATH, self.apasa_buton_salvare_locator).click()
