from selenium.webdriver.common.by import By


class LocatoriPaginaCautare:
    SEARCH_INPUT = (By.XPATH, "//*[@id='searchbox_input']")
    SEARCH_BUTTON = (By.XPATH, "//button[@aria-label='Search']//*[name()='svg']")
    RESULTS = (By.XPATH, "//*[@data-testid='mainline']//*[@data-testid='result']")
