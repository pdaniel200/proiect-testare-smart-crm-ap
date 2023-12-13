''' Clasa DashboardPage contine metodele necesare pentru a porni cronometrul, a opri cronometrul si a iesi din cont
    Metodele sunt:
    - pornire_cronometru
    - oprire_cronometru
    - iesire_cont
'''

import time
from selenium.webdriver.common.by import By
from Locators.locators import LocatoriPaginaSmartCrm
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.time = time
        # Locatori cronometru
        self.pornire_cronometru_locator = LocatoriPaginaSmartCrm.PORNIRE_CRONOMETRU_XPATH
        self.oprire_cronometru_locator = LocatoriPaginaSmartCrm.OPRIRE_CRONOMETRU_XPATH
        self.ceas_cronometru_locator = LocatoriPaginaSmartCrm.CEAS_CRONOMETRU_XPATH

        # Locatori iesire din cont
        self.buton_logout_locator = LocatoriPaginaSmartCrm.BUTON_LOGOUT_XPATH

    def pornire_cronometru(self):
        # self.driver.find_element(By.XPATH, self.pornire_cronometru_locator).click()
        # Incepe functionalitatea de cronometrare pe pagina de sarcini
        start_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.pornire_cronometru_locator)))
        start_button.click()
        # Verifica daca cronometrul a inceput
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.ceas_cronometru_locator)))
        time.sleep(2)
        # Salveaza o captura de ecran la pornirea cronometrului
        self.driver.save_screenshot("Results/test_b1_contor_pornit.png")

    def oprire_cronometru(self):
        self.driver.find_element(By.XPATH, self.oprire_cronometru_locator).click()
        # Verifică dacă cronometrul s-a oprit
        WebDriverWait(self.driver, 10).until_not(
            EC.visibility_of_element_located((By.XPATH, self.ceas_cronometru_locator)))

    def iesire_cont(self):
        self.driver.find_element(By.XPATH, self.buton_logout_locator).click()

