''' Clasa conturibancarePage contine metodele necesare pentru a adauga un cont bancar in aplicatie
    Metodele sunt:
    - adauga_cont_bancar
'''

import time
from selenium.webdriver.common.by import By
from Locators.locators import LocatoriPaginaSmartCrm
from selenium.webdriver.support import expected_conditions as EC #asertii specifice selenium pentru asteptare element vizibil
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class ConturiBancarePage:
    def __init__(self, driver):
        self.driver = driver
        self.time = time
        self.EC = EC


        # Locatori cont bancar
        self.apasa_buton_finante_locator = LocatoriPaginaSmartCrm.BUTON_FINANTE_XPATH
        self.apasa_buton_conturi_bancare_locator = LocatoriPaginaSmartCrm.BUTON_CONTURI_BANCARE_XPATH
        self.apasa_buton_adaugare_cont_bancar_locator = LocatoriPaginaSmartCrm.BUTON_ADAUGARE_CONT_BANCAR_XPATH
        self.apasa_buton_selectare_tip_cont_locator = LocatoriPaginaSmartCrm.BUTON_SELECTARE_TIP_CONT_XPATH
        self.nume_detinator_cont_locator = LocatoriPaginaSmartCrm.CAMP_NUME_DETINATOR_CONT_ID
        self.numar_contact_locator = LocatoriPaginaSmartCrm.CAMP_NUMAR_CONTACT_ID
        self.sold_deschidere_locator = LocatoriPaginaSmartCrm.CAMP_SOLD_DESCHIDERE_ID
        self.selectare_stare_cont_locator = LocatoriPaginaSmartCrm.SELECTOR_STARE_CONT_XPATH
        self.selectare_stare_cont_activ_locator = LocatoriPaginaSmartCrm.SELECTOR_STARE_CONT_ACTIV_XPATH
        self.apasa_buton_adaugare_cont_locator = LocatoriPaginaSmartCrm.BUTON_ADAUGARE_CONT_XPATH
        self.actiune_cont_locator = LocatoriPaginaSmartCrm.BUTON_ACTIUNE_CONT_XPATH
        self.sterge_cont_locator = LocatoriPaginaSmartCrm.BUTON_STERGE_CONT_XPATH
        self.confirmare_stergere_cont_locator = LocatoriPaginaSmartCrm.BUTON_CONFIRMARE_STERGERE_CONT_XPATH
        self.text_nume_detinator_cont_locator = LocatoriPaginaSmartCrm.TEXT_NUME_DETINATOR_CONT_XPATH

    def adauga_cont_bancar(self):
        self.driver.find_element(By.XPATH, self.apasa_buton_finante_locator).click()
        self.time.sleep(1)
        self.driver.find_element(By.XPATH, self.apasa_buton_conturi_bancare_locator).click()
        self.time.sleep(2)
        self.driver.find_element(By.XPATH, self.apasa_buton_adaugare_cont_bancar_locator).click()
        self.time.sleep(1)
        self.driver.find_element(By.XPATH, self.apasa_buton_selectare_tip_cont_locator).click()
        self.time.sleep(1)
        self.driver.find_element(By.ID, self.nume_detinator_cont_locator).send_keys("Test Cont")
        self.time.sleep(1)
        self.driver.find_element(By.ID, self.numar_contact_locator).send_keys("123456789")
        self.time.sleep(1)
        self.driver.find_element(By.ID, self.sold_deschidere_locator).send_keys("100")
        self.time.sleep(1)
        self.driver.find_element(By.XPATH, self.selectare_stare_cont_locator).click()
        self.time.sleep(2)
        self.driver.find_element(By.XPATH, self.selectare_stare_cont_activ_locator).click()
        self.time.sleep(2)
        self.driver.find_element(By.ID, self.apasa_buton_adaugare_cont_locator).click()
        print("Contul a fost adaugat cu succes!")
        print(f"Numele contului este: {self.driver.find_element(By.XPATH, self.text_nume_detinator_cont_locator).text}")

    def sterge_cont_bancar(self):
        self.time.sleep(2)
        self.driver.find_element(By.XPATH, self.actiune_cont_locator).click()
        self.time.sleep(2)
        print("Incepe stergerea contului bancar adaugat...")
        self.driver.find_element(By.XPATH, self.sterge_cont_locator).click()
        self.time.sleep(2)
        self.driver.find_element(By.XPATH, self.confirmare_stergere_cont_locator).click()
        self.time.sleep(2)

