from selenium.webdriver.common.by import By
from Locators.locators import LocatoriPaginaSmartCrm


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        # Locatori pagina de login
        self.username_textbox_locator = LocatoriPaginaSmartCrm.USERNAME_TEXTBOX_ID
        self.password_textbox_locator = LocatoriPaginaSmartCrm.PASSWORD_TEXTBOX_ID
        self.buton_inainte_locator = LocatoriPaginaSmartCrm.BUTON_INAINTE_ID
        self.login_button_locator = LocatoriPaginaSmartCrm.LOGIN_BUTON_ID
        self.mesaj_invalid_feedback_locator = LocatoriPaginaSmartCrm.MESAJ_INVALID_FEEDBACK_XPATH

    def enter_username(self, username):
        self.driver.find_element(By.ID, self.username_textbox_locator).clear()
        self.driver.find_element(By.ID, self.username_textbox_locator).send_keys(username)
        self.driver.find_element(By.ID, self.buton_inainte_locator).click()

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_textbox_locator).clear()
        self.driver.find_element(By.ID, self.password_textbox_locator).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.ID, self.login_button_locator).click()

    def vreificare_mesaj_parola_gresita(self):
        msg = self.driver.find_element(By.XPATH, self.mesaj_invalid_feedback_locator).text

        return msg
