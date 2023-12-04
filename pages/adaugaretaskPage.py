import time
from selenium.webdriver.common.by import By
from Locators.locators import LocatoriPaginaSmartCrm


class AdaugaTaskPage:
    def __init__(self, driver):
        self.driver = driver
        self.time = time

        # Locatori adaugare task
        self.apasa_buton_adaugare_sarcina_locator = LocatoriPaginaSmartCrm.BUTON_ADAUGARE_SARCINA_XPATH
        self.camp_titlu_sarcina_locator = LocatoriPaginaSmartCrm.CAMP_TITLU_SARCINA_ID
        self.checkbox_fara_data_scadenta_locator = LocatoriPaginaSmartCrm.CHECKBOX_FARA_DATA_SCADENTA_XPATH
        self.selector_atribuire_locator = LocatoriPaginaSmartCrm.SELECTOR_ATRIBUIRE_XPATH
        self.selecteaza_atribuire_utilizator_locator = LocatoriPaginaSmartCrm.SELECTEAZA_ATRIBUIRE_UTILIZATOR_XPATH
        self.buton_salvare_task_locator = LocatoriPaginaSmartCrm.BUTON_SALVARE_TASK_ID
        self.buton_actiune_la_task_locator = LocatoriPaginaSmartCrm.BUTON_ACTIUNE_LA_TASK_XPATH
        self.buton_sterge_task_locator = LocatoriPaginaSmartCrm.BUTON_STERGE_TASK_XPATH
        self.buton_confirmare_stergere_task_locator = LocatoriPaginaSmartCrm.BUTON_CONFIRMARE_STERGERE_TASK_XPATH



    def adauga_task_angajat(self):
        self.driver.find_element(By.XPATH, self.apasa_buton_adaugare_sarcina_locator).click()
        self.time.sleep(2)
        self.driver.find_element(By.ID, self.camp_titlu_sarcina_locator).send_keys("Sarcina Test")
        self.time.sleep(2)
        self.driver.find_element(By.XPATH, self.checkbox_fara_data_scadenta_locator).click()
        self.time.sleep(2)
        self.driver.find_element(By.XPATH, self.selector_atribuire_locator).click()
        self.time.sleep(2)
        self.driver.find_element(By.XPATH, self.selecteaza_atribuire_utilizator_locator).click()
        self.time.sleep(2)
        self.driver.find_element(By.ID, self.buton_salvare_task_locator).click()

    def sterge_task_angajat(self):

        self.driver.find_element(By.XPATH, self.buton_actiune_la_task_locator).click()
        self.time.sleep(2)
        self.driver.find_element(By.XPATH, self.buton_sterge_task_locator).click()
        self.time.sleep(2)
        self.driver.find_element(By.XPATH, self.buton_confirmare_stergere_task_locator).click()
        self.time.sleep(2)




