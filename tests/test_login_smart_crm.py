''' fisier de rulari teste
    pentru rularea testelor se foloseste comanda: pytest Tests/test_login_smart_crm.py --html=Results/report_test_login_smart_crm.html

    pentru rularea testelor cu marcarea smoke se foloseste comanda:
    pytest -k smoke --html=Results/report_test_smoke.html Tests/test_login_smart_crm.py
    pytest -m smoke --html=Results/report_test_smoke.html Tests/test_login_smart_crm.py
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

import time
from decouple import AutoConfig
import logging

# Configurare log
logging.basicConfig(level=logging.INFO) # seteaza nivelul de logare la INFO
logger = logging.getLogger(__name__) # creaza un obiect logger


class TestLoginSmartCRM(unittest.TestCase, LoginPage, DashboardPage, ConturiBancarePage, ConturiBancareTransferPage, AlocareProgramPage, AdaugaTaskPage, AdaugaComandaFurnizorPage, AdaugaCheltuialaPage):
    driver = webdriver.Chrome()

    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.title = None

    @classmethod
    def setup_class(cls):
        config = AutoConfig(search_path='.') # cauta fisierul .env in directorul curent
        cls.USERNAME = config('MAIL_UTILIZATOR')
        cls.PASSWORD = config('PAROLA')
        cls.PAROLA_GRESITA = config('PAROLA_GRESITA')

        # Inițializați o instanță Chrome WebDriver
        #cls.driver = webdriver.Chrome()
        # Seteaza asteptarea implicita
        cls.driver.implicitly_wait(10)
        # Maximizare fereastra browser pentru testare
        cls.driver.maximize_window()
        # Acceseaza pagina de conectare a aplicatiei Smart CRM
        cls.driver.get("https://app.smart-crm.ro/login")
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


    @classmethod
    def teardown_class(cls):
        # Dupa ce toate teste din clasa sunt completate, se inchide WebDriver pentru a elibera resursele
        cls.driver.quit()

    def test_a_login_valid(self):
        # Efectueaza pașii de conectare
        self.login_page.enter_username(self.USERNAME)
        time.sleep(2)
        self.login_page.enter_password(self.PASSWORD)

        # Salveaza o captura de ecran dupa oprirea cronometrului
        self.login_page.driver.save_screenshot("Results/test_a_login_page.png")
        time.sleep(2)
        # logger.info("Test Pagina Login - Logarea cu o parola valida a fost efectuata cu succes.")
        self.login_page.click_login()
        time.sleep(2)


    def test_b_contorizare_timp(self):
        # Aceseaza pagina de sarcini din cadrul aplicatiei
        self.dashboard_page.driver.get("https://app.smart-crm.ro/account/tasks")
        # scrie in log ca testul a fost efectuat cu succes
        logger.info("Test Pagina Login - Logarea cu o parola valida a fost efectuata cu succes.")
        time.sleep(4)
        # Începeți funcționalitatea de cronometrare pe pagina de sarcini
        self.dashboard_page.pornire_cronometru()
        # Salveaza o captura de ecran dupa oprirea cronometrului
        self.dashboard_page.driver.save_screenshot("Results/test_b_contor_pornit.png")
        # scrie in log ca testul a fost efectuat cu succes
        logger.info("Testare Pagina Sarcini - Pornire cronometru efectuat cu succes.")
        time.sleep(6)

        # Opreste funcționalitatea de cronometrare pe pagina de sarcini
        self.dashboard_page.oprire_cronometru()

        # Salveaza o captura de ecran dupa oprirea cronometrului
        self.dashboard_page.driver.save_screenshot("Results/test_b_contor_oprit.png")
        # scrie in log ca testul a fost efectuat cu succes
        logger.info("Test Pagina Sarcini - Oprire cronometru efectuat cu succes.")
        time.sleep(6)

    def test_c_adaugare_cont_bancar(self):
        self.conturibancare_page.adauga_cont_bancar()
        time.sleep(2)
        self.conturibancare_page.driver.save_screenshot("Results/test_c_adaugare_cont_bancar.png")
        # scrie in log ca testul a fost efectuat cu succes
        logger.info("Test adaugare cont bancar - Efectuat cu succes.")


    def test_d_transfer_intre_conturi(self):
        self.conturibancaretransfer_page.transfera_intre_conturi()
        time.sleep(2)
        # scrie in log ca testul a fost efectuat cu succes
        logger.info("Testare transfer intre conturi bancare - Efectuat cu succes.")
        self.conturibancaretransfer_page.driver.save_screenshot("Results/test_d_transfer_intre_conturi.png")


    def test_e_alocare_program_angajat(self):
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
        self.adaugarecomandafurnizor_page.adauga_comanda_furnizor()
        time.sleep(2)
        self.adaugarecomandafurnizor_page.driver.save_screenshot("Results/test_g_adaugare_comanda_furnizor.png")
        # scrie in log ca testul a fost efectuat cu succes
        logger.info("Test adaugare comanda furnizor - Efectuat cu succes.")
        time.sleep(2)


    def test_h_adaugare_cheltuiala(self):
        self.adaugarecheltuiala_page.adauga_cheltuiala()
        time.sleep(2)
        self.adaugarecheltuiala_page.driver.save_screenshot("Results/test_h_adaugare_cheltuiala.png")
        # scrie in log ca testul a fost efectuat cu succes
        logger.info("Test adaugare cheltuiala - Efectuat cu succes.")
        time.sleep(2)


    def test_i_adaugare_bunuri(self):
        pass



    def test_j_iesire_cont(self):
        # Efectuați pașii de deconectare
        self.dashboard_page.iesire_cont()
        time.sleep(2)

        # Log information about the successful completion of the test
        logger.info("Testare iesire din cont - Iesirea din cont a fost efectuata cu succes.")

    def test_k_login_invalid_password(self):
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
        self.login_page.driver.save_screenshot("Results/test_login_invalid_pass.png")
        time.sleep(2)
        # Log information about the successful completion of the test
        logger.info("Testare Pagina Login - Test login si returnare mesaj a fost efectuat cu succes.")






    '''@pytest.mark.smoke
    def test_smoke_title(browser):
        # Deschide pagina web
        browser.get("https://app.smart-crm.ro/login")

        # Verifică titlul paginii
        assert "SMART CRM" in browser.title'''

