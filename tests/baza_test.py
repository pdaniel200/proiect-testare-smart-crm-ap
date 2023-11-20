# Importare module necesare
import os
import warnings
from pathlib import Path

import pytest
import yaml

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service as ServiceChrome
from selenium.webdriver.firefox.service import Service as ServiceFirefox
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

# configurare nivel de log pentru webdriver manager
os.environ['WDM_LOG_LEVEL'] = '0'


# functie pentru citire configurație din config.yaml
def config():
    # stabilirea caii catre fisierul de configurare YAML
    path = Path(__file__).parent / "../data/config.yaml"
    try:
        # deschiderea si citirea fisierului YAML
        with open(path) as config_file:
            # incarcarea continutului fisierului YAML intr-un obiect de date
            data = yaml.load(config_file, Loader=yaml.FullLoader)
        return data
    finally:
        # inchiderea fisierului in blocul 'finally'
        config_file.close()


# clasa de baza pentru teste
class PrincipalulTest:

    @pytest.fixture(autouse=True)  # decorator Pytest care transforma o functie obisnuita in fixture
    def initializare_driver(self):
        warnings.simplefilter("ignore", ResourceWarning)  # dezactivare avertismente
        if config()['browser'] == 'chrome':  # verificare tip de browser ales in fisierul de configurare config.yaml
            options = webdriver.ChromeOptions()
            if config()['headless']:  # adaugare opțiuni pentru mod fara interfata grafica
                options.add_argument('--headless')
                options.add_argument('--no-sandbox')
                options.add_argument('--disable-gpu')
                options.add_argument('--window-size=1920,1080')
            # initializare driver chrome
            self.driver = webdriver.Chrome(service=ServiceChrome(ChromeDriverManager().install()), options=options)
        elif config()['browser'] == 'firefox':  # verificare tip de browser ales in fisierul de configurare config.yaml
            options = webdriver.FirefoxOptions()
            if config()['headless']:  # adaugare opțiuni pentru mod fara interfata grafica la browserul firefox
                options.add_argument('--headless')
                options.add_argument('--no-sandbox')
                options.add_argument('--disable-gpu')
                options.add_argument('--window-size=1920,1080')
            # initializare driver firefox
            self.driver = webdriver.Firefox(service=ServiceFirefox(GeckoDriverManager().install()), options=options)
        else:
            raise Exception("Nu sunt configurari pentru  tipul de browser ales din config.yaml")

        self.driver.maximize_window()  # maximizare fereastra browser
        self.wait = WebDriverWait(self.driver, 5)  # asteptare timp de 5 secunde
        yield self.wait, self.driver  # rulare test

        if self.driver is not None:  # inchidere driver după incheierea testului
            self.driver.close()
            self.driver.quit()
