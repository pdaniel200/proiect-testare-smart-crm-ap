''' Modul pentru configurarea driverului de browser
    Acest modul este folosit pentru a configura driverul de browser
    in functie de parametrii din fisierul de configurare config.yaml
'''

# Importare module necesare
import os
import warnings
from pathlib import Path

import yaml

from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service as ServiceChrome
from selenium.webdriver.firefox.service import Service as ServiceFirefox

from selenium.webdriver.edge.service import Service as ServiceEdge
from selenium.webdriver.edge.options import Options as OptionsEdge

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
# from webdriver_manager.microsoft import IEDriverManager

# configurare nivel de log pentru webdriver manager
os.environ['WDM_LOG_LEVEL'] = '0'

# functie pentru citire configurație din config.yaml
def config():
    path = Path(__file__).parent / "../Data/config.yaml"
    with open(path) as config_file:
        data = yaml.load(config_file, Loader=yaml.FullLoader)
    return data


# clasa configurare driver
class ConfigurareDriver:
    @staticmethod
    def initializare_driver():
        '''Metoda pentru initializarea driverului de browser in functie de parametrii din fisierul de configurare config.yaml
        '''
        warnings.simplefilter("ignore", ResourceWarning)
        if config()['browser'] == 'chrome': # verificare tip de browser
            options = webdriver.ChromeOptions()
            if config()['headless']:  # adaugare opțiuni pentru mod fara interfata grafica la browserul chrome
                options.add_argument('--headless')
                options.add_argument('--no-sandbox')
                options.add_argument('--disable-gpu')
                options.add_argument('--window-size=1920,1080')
            if config()['webdriver'] == 'local': # verificare tip de driver
                chrome_driver_path = Path(__file__).parent / "../drvweb/chromedriver.exe"
                chrome_service = ServiceChrome(chrome_driver_path)
            else:
                chrome_service = ServiceChrome(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=chrome_service, options=options)
            driver.maximize_window()
            return driver
        elif config()['browser'] == 'firefox': # verificare tip de browser
            options = webdriver.FirefoxOptions()
            if config()['headless']:  # adaugare opțiuni pentru mod fara interfata grafica la browserul firefox
                options.add_argument('--headless')
                options.add_argument('--no-sandbox')
                options.add_argument('--disable-gpu')
                options.add_argument('--window-size=1920,1080')
            if config()['webdriver'] == 'local': # verificare tip de driver
                firefox_driver_path = Path(__file__).parent / "../drvweb/geckodriver.exe"
                firefox_service = ServiceFirefox(firefox_driver_path)
            else:
                firefox_service = ServiceFirefox(GeckoDriverManager().install())
            driver = webdriver.Firefox(service=firefox_service, options=options)
            driver.maximize_window()
            return driver
        elif config()['browser'] == 'edge': # verificare tip de browser
            options = OptionsEdge()
            if config()['headless']:  # adaugare opțiuni pentru mod fara interfata grafica la browserul edge
                options.add_argument('--headless')
                options.add_argument('--no-sandbox')
                options.add_argument('--disable-gpu')
                options.add_argument('--window-size=1920,1080')
            if config()['webdriver'] == 'local': # verificare tip de driver
                edge_driver_path = Path(__file__).parent / "../drvweb/msedgedriver.exe"
                edge_service = ServiceEdge(edge_driver_path)
            else:
                edge_service = ServiceEdge(EdgeChromiumDriverManager().install())
            driver = webdriver.Edge(service=edge_service, options=options)
            driver.maximize_window()
            return driver
        else:
            raise Exception("Tip de browser nespecificat in config.yaml") # eroare daca tipul de browser nu este specificat in fisierul de configurare

