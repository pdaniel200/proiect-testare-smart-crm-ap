from selenium.webdriver.common.by import By


class LocatoriPaginaCautare:
    BUTON_AUTENTIFICARE = (By.XPATH, "//a[@class='action_button top-bar-right-button ']")
    USERNAME_INPUT = (By.ID, "email")
    BUTON_INAINTE = (By.XPATH, "//button[@id='submit-next']")
    #APARE_INPUT = (By.XPATH, "//input[@id='password']")
    PASSWORD_INPUT = (By.ID, "password")
    BUTON_LOGIN = (By.ID, "submit-login")
    APARE_PAGINA = (By.XPATH, "//a[@title='Panou Utilizator']")
    PORNIRE_CRONOMETRU = (By.XPATH, "//i[@class='bi bi-play-circle-fill']")
    OPRIRE_CRONOMETRU = (By.XPATH, "//i[@class='bi bi-stop-circle-fill']")
    BUTON_LOGOUT = (By.XPATH, "//a[@class='d-block header-icon-box']//*[name()='svg']//*[name()='path' and contains(@fill,'currentCol')]")
