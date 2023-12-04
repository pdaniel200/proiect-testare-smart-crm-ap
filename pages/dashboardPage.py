import time
from selenium.webdriver.common.by import By
from Locators.locators import LocatoriPaginaSmartCrm


class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.time = time

        # Locatori cronometru
        self.pornire_cronometru_locator = LocatoriPaginaSmartCrm.PORNIRE_CRONOMETRU_XPATH
        self.oprire_cronometru_locator = LocatoriPaginaSmartCrm.OPRIRE_CRONOMETRU_XPATH

        # Locatori iesire cont
        self.buton_logout_locator = LocatoriPaginaSmartCrm.BUTON_LOGOUT_XPATH

    def pornire_cronometru(self):
        self.driver.find_element(By.XPATH, self.pornire_cronometru_locator).click()
    def oprire_cronometru(self):
        self.driver.find_element(By.XPATH, self.oprire_cronometru_locator).click()
    def iesire_cont(self):
        self.driver.find_element(By.XPATH, self.buton_logout_locator).click()