''' fisier de rulari teste
    pentru rularea testelor se foloseste comanda:
    pytest Tests/test_smart_crm_config.py --html=Results/report_test_smart_crm_config.html
    pentru rularea testelor cu marcarea smoke se foloseste comanda:
    pytest -k smoke --html=Results/report_test_smoke.html Tests/test_smart_crm_config.py
'''

import unittest
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from Pages.dashboardPage import DashboardPage
from Pages.loginPage import LoginPage
from Pages.conturibancarePage import ConturiBancarePage
from Pages.conturibancaretransferPages import ConturiBancareTransferPage
from Pages.alocareprogramPage import AlocareProgramPage
from Pages.adaugaretaskPage import AdaugaTaskPage
from Pages.adaugarecomandafurnizorPage import AdaugaComandaFurnizorPage
from Pages.adaugarecheltuialaPage import AdaugaCheltuialaPage
from Pages.adaugarebunuriPage import AdaugaBunuriPage

import time
from decouple import AutoConfig
import logging

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Data.configurare_driver import ConfigurareDriver

# Configurare log
logging.basicConfig(level=logging.INFO) # seteaza nivelul de logare la INFO
logger = logging.getLogger(__name__) # creaza un obiect logger


class TestLoginSmartCRM(ConfigurareDriver, unittest.TestCase, LoginPage, DashboardPage, ConturiBancarePage, ConturiBancareTransferPage, AlocareProgramPage, AdaugaTaskPage, AdaugaComandaFurnizorPage, AdaugaCheltuialaPage, AdaugaBunuriPage):
    wait = None # variabila pentru asteptare

    def __init__(self, methodName: str = ...):
        '''Metoda care se executa inainte de fiecare test din clasa'''
        super().__init__(methodName)
        self.title = None

    @classmethod
    def setUpClass(cls):
        '''Metoda care se executa inainte de rularea tuturor testelor din clasa'''
        cls.driver = ConfigurareDriver.initializare_driver()  # initializare driver

        config = AutoConfig(search_path='.') # cauta fisierul .env in directorul curent
        cls.USERNAME = config('MAIL_UTILIZATOR')
        cls.PASSWORD = config('PAROLA')
        cls.PAROLA_GRESITA = config('PAROLA_GRESITA')
        cls.wait = WebDriverWait(cls.driver, 10) # seteaza timpul de asteptare la 10 secunde pentru elementele din pagina
        # Creeaza instante pentru clasele LoginPage, DashboardPage si restul paginilor
        cls.login_page = LoginPage(cls.driver)
        cls.dashboard_page = DashboardPage(cls.driver)
        cls.conturibancare_page = ConturiBancarePage(cls.driver)
        cls.conturibancaretransfer_page = ConturiBancareTransferPage(cls.driver)
        cls.mesaj_invalid_feedback_locator = "//div[@class='invalid-feedback']"
        cls.alocareprogram_page = AlocareProgramPage(cls.driver)
        cls.adaugaretask_page = AdaugaTaskPage(cls.driver)
        cls.adaugarecomandafurnizor_page = AdaugaComandaFurnizorPage(cls.driver)
        cls.adaugarecheltuiala_page = AdaugaCheltuialaPage(cls.driver)
        cls.adaugarebunuri_page = AdaugaBunuriPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        '''Metoda care se executa dupa rularea tuturor testelor din clasa'''
        cls.driver.quit()

    def test_a_login_valid(self):
        '''Metoda care efectueaza testarea paginii de login cu o parola valida'''
        self.login_page.driver.get("https://app.smart-crm.ro/login")
        self.login_page.enter_username(self.USERNAME) # introducere username
        time.sleep(3)
        self.login_page.enter_password(self.PASSWORD) # introducere parola
        self.login_page.driver.save_screenshot("Results/test_a_login_page.png") # Salveaza o captura de ecran dupa oprirea cronometrului
        time.sleep(3)
        self.login_page.click_login()
        time.sleep(3)

    def test_b_contorizare_timp(self):
        '''Metoda care efectueaza testarea paginii de sarcini cu cronometrul pornit si oprit'''
        # Aceseaza pagina de sarcini din cadrul aplicatiei
        self.dashboard_page.driver.get("https://app.smart-crm.ro/account/tasks")
        # Scrie in log ca testul a fost efectuat cu succes
        logger.info("Test Pagina Login - Logarea cu o parola valida a fost efectuata cu succes.")
        time.sleep(4)
        # Începeți funcționalitatea de cronometrare pe pagina de sarcini
        self.dashboard_page.pornire_cronometru()
        # Salveaza o captura de ecran dupa oprirea cronometrului
        self.dashboard_page.driver.save_screenshot("Results/test_b_contor_oprit.png")
        # Scrie in log ca testul a fost efectuat cu succes
        logger.info("Testare Pagina Sarcini - Pornire cronometru efectuat cu succes.")
        time.sleep(6)

        # Opreste funcționalitatea de cronometrare pe pagina de sarcini
        self.dashboard_page.oprire_cronometru()

        # Salveaza o captura de ecran dupa oprirea cronometrului
        self.dashboard_page.driver.save_screenshot("Results/test_b_contor_pornit.png")
        # scrie in log ca testul a fost efectuat cu succes
        logger.info("Test Pagina Sarcini - Oprire cronometru efectuat cu succes.")
        time.sleep(6)

    def test_c_adaugare_cont_bancar(self):
        '''Metoda care efectueaza testarea paginii de conturi bancare cu adaugare cont bancar'''
        self.conturibancare_page.adauga_cont_bancar()
        time.sleep(2)
        self.conturibancare_page.driver.save_screenshot("Results/test_c_adaugare_cont_bancar.png")
        # scrie in log ca testul a fost efectuat cu succes
        logger.info("Test adaugare cont bancar - Efectuat cu succes.")

    def test_d_transfer_intre_conturi(self):
        '''Metoda care efectueaza testarea paginii de conturi bancare cu transfer intre conturi'''
        self.conturibancaretransfer_page.transfera_intre_conturi()
        time.sleep(2)
        # scrie in log ca testul a fost efectuat cu succes
        logger.info("Testare transfer intre conturi bancare - Efectuat cu succes.")
        self.conturibancaretransfer_page.driver.save_screenshot("Results/test_d_transfer_intre_conturi.png")

    def test_e_alocare_program_angajat(self):
        '''Metoda care efectueaza testarea paginii de alocare program angajat'''
        self.alocareprogram_page.adauga_program_angajat()
        time.sleep(2)
        # scrie in log ca testul a fost efectuat cu succes
        logger.info("Test alocare program angajat - Efectuat cu succes.")
        self.alocareprogram_page.driver.save_screenshot("Results/test_e_alocare_program_angajat.png")
        self.alocareprogram_page.sterge_program_angajat()
        time.sleep(2)
        # scrie in log ca testul a fost efectuat cu succes
        logger.info("Test stergere program angajat - Efectuat cu succes.")
        time.sleep(2)

    def test_f_adaugare_task(self):
        '''Metoda care efectueaza testarea paginii de adaugare task'''
        # Aceseaza pagina de sarcini din cadrul aplicatiei
        self.adaugaretask_page.driver.get("https://app.smart-crm.ro/account/tasks")
        time.sleep(4)
        self.adaugaretask_page.adauga_task_angajat()
        time.sleep(2)
        self.adaugaretask_page.driver.save_screenshot("Results/test_f_adaugare_task.png")
        # scrie in log ca testul a fost efectuat cu succes
        logger.info("Test adaugare task - Efectuat cu succes.")
        time.sleep(2)
        self.adaugaretask_page.sterge_task_angajat()
        time.sleep(2)
        # scrie in log ca testul a fost efectuat cu succes
        logger.info("Test stergere task - Efectuat cu succes.")

    def test_g_adaugare_comanda_furnizor(self):
        '''Metoda care efectueaza testarea paginii de adaugare comanda furnizor'''
        self.adaugarecomandafurnizor_page.adauga_comanda_furnizor()
        time.sleep(2)
        self.adaugarecomandafurnizor_page.driver.save_screenshot("Results/test_g_adaugare_comanda_furnizor.png")
        # scrie in log ca testul a fost efectuat cu succes
        logger.info("Test adaugare comanda furnizor - Efectuat cu succes.")
        time.sleep(2)

    def test_h_adaugare_cheltuiala(self):
        '''Metoda care efectueaza testarea paginii de adaugare cheltuiala'''
        self.adaugarecheltuiala_page.adauga_cheltuiala()
        time.sleep(2)
        self.adaugarecheltuiala_page.driver.save_screenshot("Results/test_h_adaugare_cheltuiala.png")
        # scrie in log ca testul a fost efectuat cu succes
        logger.info("Test adaugare cheltuiala - Efectuat cu succes.")
        time.sleep(2)

    def test_i_adaugare_bunuri(self):
        '''Metoda care efectueaza testarea paginii de adaugare bunuri'''
        self.adaugarebunuri_page.adauga_active_bunuri()
        time.sleep(2)
        self.adaugarebunuri_page.driver.save_screenshot("Results/test_i_adaugare_bunuri.png")
        # scrie in log ca testul a fost efectuat cu succes
        logger.info("Test adaugare bunuri - Efectuat cu succes.")
        time.sleep(2)
        self.adaugarebunuri_page.sterge_active_bunuri()
        time.sleep(2)
        # scrie in log ca testul a fost efectuat cu succes
        logger.info("Test stergere bunuri - Efectuat cu succes.")
        time.sleep(2)

    def test_j_iesire_cont(self):
        '''Metoda care efectueaza testarea paginii de iesire din cont'''
        # Efectuați pașii de deconectare
        self.dashboard_page.iesire_cont()
        time.sleep(2)

        # scrie in log ca testul a fost efectuat cu succes
        logger.info("Testare iesire din cont - Iesirea din cont a fost efectuata cu succes.")

    def test_k_login_invalid_password(self):
        '''Metoda care efectueaza testarea paginii de login cu o parola invalida'''
        # Efectuați pașii de conectare
        self.login_page.enter_username(self.USERNAME)
        time.sleep(2)
        self.login_page.enter_password(self.PAROLA_GRESITA)
        time.sleep(1)
        self.login_page.click_login()
        message = self.driver.find_element(By.XPATH, self.mesaj_invalid_feedback_locator).text
        self.assertEqual(message, "Aceste acreditări nu se potrivesc cu înregistrările noastre.")
        time.sleep(1)
        # Salvați o captură de ecran a paginii de conectare cu mesajul parola greșită
        self.login_page.driver.save_screenshot("Results/test_j_login_invalid_pass.png")
        time.sleep(2)
        # scrie in log ca testul a fost efectuat cu succes
        logger.info("Testare Pagina Login - Test login si returnare mesaj a fost efectuat cu succes.")



    @pytest.mark.skip(reason="Nu mai este necesar")
    def test_titlu_pg_principala(self):
        self.driver.get("https://smart-crm.ro/")
        assert "Smart CRM" in self.driver.title

    @pytest.mark.smoke() # marcarea testului ca smoke
    def test_smoke_title(self):
        self.driver.get("https://app.smart-crm.ro/login")
        assert "SMART CRM" in self.driver.title

if __name__ == '__main__': # rulare test in mod standalone
    unittest.main()