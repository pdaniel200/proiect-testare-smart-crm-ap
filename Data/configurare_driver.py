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
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service as ServiceChrome
from selenium.webdriver.firefox.service import Service as ServiceFirefox
from selenium.webdriver.edge.service import Service as ServiceEdge
from selenium.webdriver.edge.options import Options as OptionsEdge

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager


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
        warnings.simplefilter("ignore", ResourceWarning)
        if config()['browser'] == 'chrome':
            options = webdriver.ChromeOptions()
            if config()['headless']:  # adaugare opțiuni pentru mod fara interfata grafica
                options.add_argument('--headless')
                options.add_argument('--no-sandbox')
                options.add_argument('--disable-gpu')
                options.add_argument('--window-size=1920,1080')
            driver = webdriver.Chrome(service=ServiceChrome(ChromeDriverManager().install()), options=options)
            driver.maximize_window()
            return driver
        elif config()['browser'] == 'firefox':
            options = webdriver.FirefoxOptions()
            if config()['headless']:  # adaugare opțiuni pentru mod fara interfata grafica la browserul firefox
                options.add_argument('--headless')
                options.add_argument('--no-sandbox')
                options.add_argument('--disable-gpu')
                options.add_argument('--window-size=1920,1080')
            driver = webdriver.Firefox(service=ServiceFirefox(GeckoDriverManager().install()), options=options)
            driver.maximize_window()
            return driver
        elif config()['browser'] == 'ie':
            options = webdriver.IeOptions()
            # path = "Driversw/IEDriverServer.exe"
            if config()['headless']:  # adaugare opțiuni pentru mod fara interfata grafica la browserul firefox
                options.add_argument('--headless')
                options.add_argument('--no-sandbox')
                options.add_argument('--disable-gpu')
                options.add_argument('--window-size=1920,1080')
            driver = webdriver.Ie(service=ServiceChrome(IEDriverManager().install()), options=options)
            driver.maximize_window()
            return driver
        elif config()['browser'] == 'edge':
            options = webdriver.EdgeOptions()
            # options.use_chromium = True
            if config()['headless']:  # adaugare opțiuni pentru mod fara interfata grafica la browserul firefox
                options.add_argument('--headless')
                options.add_argument('--no-sandbox')
                options.add_argument('--disable-gpu')
                options.add_argument('--window-size=1920,1080')

            edge_driver_path = Path(__file__).parent / "../drvweb/msedgedriver.exe"
            edge_service = ServiceEdge(edge_driver_path)
            edge_options = OptionsEdge()

            driver = webdriver.Edge(service=edge_service, options=edge_options)
            driver.maximize_window()
            return driver
        else:
            raise Exception("Tip de browser nespecificat in config.yaml")
