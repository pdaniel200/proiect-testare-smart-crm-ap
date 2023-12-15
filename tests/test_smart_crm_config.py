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
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

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
import re

from Data.configurare_driver import ConfigurareDriver

# Configurare log
logging.basicConfig(level=logging.INFO) # seteaza nivelul de logare la INFO
logger = logging.getLogger(__name__) # creaza un obiect logger


class TestLoginSmartCRM(ConfigurareDriver, unittest.TestCase, LoginPage, DashboardPage, ConturiBancarePage, ConturiBancareTransferPage, AlocareProgramPage, AdaugaTaskPage, AdaugaComandaFurnizorPage, AdaugaCheltuialaPage, AdaugaBunuriPage):
    # driver = None
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
        # cls.mesaj_invalid_feedback_locator = "//div[@class='invalid-feedback']"
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
        self.login_page.driver.save_screenshot("Results/test_a_login_page.png") # Salveaza o captura de ecran a paginii de conectare
        time.sleep(3)
        self.login_page.click_login()
        message = self.driver.find_element(By.XPATH, self.login_page.mesaj_intampinare_dashboard_locator).text
        # Verifica daca mesajul de intampinare este cel asteptat
        self.assertEqual(message, "Bine ați venit test", "Mesajul de intampinare nu este cel asteptat.")
        # scrie in log ca testul a fost efectuat cu succes
        print(f'Mesajul de intampinare este: {message}')
        logger.info(f"Test Pagina Login - Logarea cu o parola valida a fost efectuata cu succes. Mesaj: {message}")
        time.sleep(3)

    def test_b_contorizare_timp(self):
        '''Metoda care efectueaza testarea paginii de sarcini cu cronometrul pornit si oprit'''
        try:
            # Aceseaza pagina de sarcini din cadrul aplicatiei
            self.dashboard_page.driver.get("https://app.smart-crm.ro/account/tasks")
            self.dashboard_page.pornire_cronometru()

            # Verifica prezenta ceasului de cronometru pentru sarcini
            ceas_taskuri = self.dashboard_page.driver.find_element(By.XPATH, self.dashboard_page.ceas_cronometru_locator)
            self.assertIsNotNone(ceas_taskuri, "Cronometrul nu a inceput.")
            logger.info("Testare Pagina Sarcini - Pornire cronometru efectuat cu succes.")
            time.sleep(6)

            # Oprire cronometru
            self.dashboard_page.oprire_cronometru()
            logger.info("Test Pagina Sarcini - Oprire cronometru a fost efectuată cu succes.")
            time.sleep(2)
            # Salveaza o captura de ecran dupa oprirea cronometrului
            self.dashboard_page.driver.save_screenshot("Results/test_b2_contor_oprit.png")

        except TimeoutException as e: # exceptie pentru cazul in care cronometrul nu a pornit
            logger.error("Testarea cronometrului a eșuat: " + str(e))
            self.fail("Cronometrul nu a functionat corespunzator.")

    def test_c_adaugare_cont_bancar(self):
        '''Metoda care efectueaza testarea paginii de conturi bancare cu adaugare cont bancar'''
        self.conturibancare_page.adauga_cont_bancar()
        # Asteapta pana cand contul adaugat este cel asteptat
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.XPATH, self.conturibancare_page.text_nume_detinator_cont_locator), "Test Cont"))
        # Verifica daca contul adaugat este cel asteptat
        cont_adaugat = self.driver.find_element(By.XPATH, self.conturibancare_page.text_nume_detinator_cont_locator).text
        self.assertEqual(cont_adaugat, "Test Cont", "Contul adaugat nu este cel asteptat.")
        self.conturibancare_page.driver.save_screenshot("Results/test_c_adaugare_cont_bancar.png")
        logger.info("Test adaugare cont bancar - Efectuat cu succes.")
        # Sterge contul adaugat
        self.conturibancare_page.sterge_cont_bancar()

    def test_d_transfer_intre_conturi(self):
        '''Metoda care efectueaza testarea paginii de conturi bancare cu transfer intre conturi'''
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.XPATH, self.conturibancaretransfer_page.text_nume_detinator_cont1_locator),
                                             "cont 1 companie"))
        self.driver.find_element(By.XPATH, self.conturibancaretransfer_page.apasa_nume_detinator_cont_locator).click()
        time.sleep(2)
        valoare_cont = self.driver.find_element(By.XPATH, self.conturibancaretransfer_page.sold_cont_bancar_locator).text
        # Extragere numere din string
        valoare_cont_initial_cifre = re.search(r'(\d+,\d+\.\d+|\d+\.\d+|\d+)', valoare_cont)
        valoare_cont_initial_c = float(valoare_cont_initial_cifre.group(0).replace(',', ''))
        print(f'valoare_cont_initial: {valoare_cont_initial_c}')
        self.conturibancaretransfer_page.transfera_intre_conturi()
        time.sleep(4)
        valoare_cont_dupa_transfer = self.driver.find_element(By.XPATH, self.conturibancaretransfer_page.sold_cont_bancar_locator).text
        # Extragere numere din string
        valoare_cont_dupa_transfer_cifre = re.search(r'(\d+,\d+\.\d+|\d+\.\d+|\d+)', valoare_cont_dupa_transfer)
        valoare_cont_dupa_transfer_c = float(valoare_cont_dupa_transfer_cifre.group(0).replace(',', ''))
        print(f'valoare_cont_dupa transfer: {valoare_cont_dupa_transfer_c}')
        # Verifica daca transferul a fost efectuat cu succes
        self.assertEqual(valoare_cont_initial_c, valoare_cont_dupa_transfer_c + 10, "Transferul nu a fost efectuat cu succes.")
        # scrie in log ca testul a fost efectuat cu succes
        logger.info("Testare transfer intre conturi bancare - Efectuat cu succes. Pentru verificare am facut un transfer de 10 lei si am verificat daca valoarea contului a scazut cu valoarea transferata.")
        self.conturibancaretransfer_page.driver.save_screenshot("Results/test_d_transfer_intre_conturi.png")

    def test_e_alocare_program_angajat(self):
        '''Metoda care efectueaza testarea paginii de alocare program angajat'''

        self.alocareprogram_page.adauga_program_angajat()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, self.alocareprogram_page.mesaj_notificari_sistem_locator), "Schimbul angajatului a fost salvat."))
        mesaj_notificare_sistem = self.driver.find_element(By.XPATH, self.alocareprogram_page.mesaj_notificari_sistem_locator).text
        self.assertEqual(mesaj_notificare_sistem, 'Schimbul angajatului a fost salvat.')
        # scrie in log ca testul a fost efectuat cu succes
        logger.info("Test alocare program angajat - Efectuat cu succes. Pentru verificare am adaugat un program de lucru pentru prima zi a lunii curente si am verificat daca s-a salvat prin verificarea mesajului de notificare.")
        self.alocareprogram_page.driver.save_screenshot("Results/test_e_alocare_program_angajat.png")
        time.sleep(2)
        self.alocareprogram_page.sterge_program_angajat()
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.XPATH, self.alocareprogram_page.mesaj_notificari_sistem_locator),
                                             "S-a șters cu succes."))
        mesaj_notificare_sistem = self.driver.find_element(By.XPATH,
                                                           self.alocareprogram_page.mesaj_notificari_sistem_locator).text
        self.assertEqual(mesaj_notificare_sistem, 'S-a șters cu succes.', "Mesajul de notificare nu este cel asteptat.")
        # scrie in log ca programul a fost sters cu succes
        logger.info("Test stergere program angajat - Efectuat cu succes.")
        time.sleep(2)

    # @pytest.mark.smoke()  # test smoke
    def test_f_adaugare_task(self):

        '''Metoda care efectueaza testarea paginii de adaugare task'''
        # Aceseaza pagina de sarcini din cadrul aplicatiei
        self.adaugaretask_page.driver.get("https://app.smart-crm.ro/account/tasks")
        time.sleep(4)
        self.adaugaretask_page.adauga_task_angajat()
        # Asteapta pana cand taskul adaugat este cel asteptat
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.XPATH, self.adaugaretask_page.text_task_nou_adaugat_locator),
                                             "Sarcina Test"))
        # Verifica daca taskul adaugat este cel asteptat
        task_adaugat = self.driver.find_element(By.XPATH,
                                                self.adaugaretask_page.text_task_nou_adaugat_locator).text
        self.assertEqual(task_adaugat, "Sarcina Test", "Numele taskului adaugat nu este cel asteptat.")
        self.adaugaretask_page.driver.save_screenshot("Results/test_f_adaugare_task.png")
        # scrie in log ca testul a fost efectuat cu succes
        logger.info("Test adaugare task - Efectuat cu succes. Pentru verificare am adaugat un task si am verificat daca exista in lista de taskuri")
        time.sleep(2)
        self.adaugaretask_page.sterge_task_angajat()
        time.sleep(2)
        # scrie in log ca taskul a fost sters cu succes
        logger.info("Test stergere task - Efectuat cu succes.")

    def test_g_adaugare_comanda_furnizor(self):
        '''Metoda care efectueaza testarea paginii de adaugare comanda furnizor'''
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.adaugarecomandafurnizor_page.buton_meniu_achizitii_locator).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.adaugarecomandafurnizor_page.buton_meniu_comenzi_furnizori_locator).click()
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(
                (By.XPATH, self.adaugarecomandafurnizor_page.text_numar_comanda_locator),
                "PO#002"))
        time.sleep(2)
        numar_ultima_comanda = self.driver.find_element(By.XPATH, self.adaugarecomandafurnizor_page.text_numar_comanda_locator).text
        # Extragere numere din string
        numar_ultima_comanda_str = re.search(r'\d+', numar_ultima_comanda)
        numar_ultima_comanda_int = int(numar_ultima_comanda_str.group())
        print(f'Ultimul numar inainte de adaugare comanda: {numar_ultima_comanda_int}')
        self.adaugarecomandafurnizor_page.adauga_comanda_furnizor()
        time.sleep(2)
        numar_comanda_noua = self.driver.find_element(By.XPATH, self.adaugarecomandafurnizor_page.text_numar_comanda_locator).text
        # Extragere numere din string
        numar_comanda_noua_str = re.search(r'\d+', numar_comanda_noua)
        numar_comanda_noua_int = int(numar_comanda_noua_str.group())
        print(f'Ultimul numar dupa adaugare comanda: {numar_comanda_noua_int}')
        # Verifica daca comanda a fost adaugata cu succes
        self.assertEqual(numar_comanda_noua_int, numar_ultima_comanda_int + 1, "Numarul comenzii nu a fost incrementat cu o unitate.")
        self.adaugarecomandafurnizor_page.driver.save_screenshot("Results/test_g_adaugare_comanda_furnizor.png")
        time.sleep(2)
        self.adaugarecomandafurnizor_page.sterge_comanda_furnizor()
        # scrie in log ca testul a fost efectuat cu succes
        logger.info("Test adaugare comanda furnizor - Efectuat cu succes. Pentru verificare am adaugat o comanda si am verificat daca numarul a fost incrementat cu o unitate.")
        time.sleep(2)

    def test_h_adaugare_cheltuiala(self):
        '''Metoda care efectueaza testarea paginii de adaugare cheltuiala'''
        self.adaugarecheltuiala_page.adauga_cheltuiala()
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.XPATH, self.adaugarecheltuiala_page.nume_cheltuiala_locator),
                                             "Cheltuiala Test"))
        # Verifica daca cheltuiala adaugata este cea asteptata
        nume_cheltuiala = self.driver.find_element(By.XPATH,
                                                self.adaugarecheltuiala_page.nume_cheltuiala_locator).text
        self.assertEqual(nume_cheltuiala, "Cheltuiala Test", "Numele cheltuielii adaugate nu este cel asteptat.")
        self.adaugarecheltuiala_page.driver.save_screenshot("Results/test_h_adaugare_cheltuiala.png")

        self.adaugarecheltuiala_page.sterge_cheltuiala()
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.XPATH, self.adaugarecheltuiala_page.mesaj_notificari_sistem_stergere_locator),
                                             "S-a șters cu succes."))
        mesaj_notificare_sistem = self.driver.find_element(By.XPATH,
                                                           self.adaugarecheltuiala_page.mesaj_notificari_sistem_stergere_locator).text
        self.assertEqual(mesaj_notificare_sistem, 'S-a șters cu succes.')
        # scrie in log ca testul a fost efectuat cu succes
        logger.info("Test adaugare + stergere cheltuiala - Efectuat cu succes. Pentru verificare am adaugat o cheltuiala si am verificat daca exista in lista de cheltuieli si am sters-o.")
        time.sleep(2)

    def test_i_adaugare_bunuri(self):
        '''Metoda care efectueaza testarea paginii de adaugare bunuri'''
        self.adaugarebunuri_page.adauga_active_bunuri()
        # Asteapta pana cand acciza adaugata este cea asteptata
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.XPATH, self.adaugarebunuri_page.text_denumire_bun_locator),
                                             "Bun Test"))
        # Verifica daca acciza adaugata este cea asteptata
        bun_adaugat = self.driver.find_element(By.XPATH,
                                                self.adaugarebunuri_page.text_denumire_bun_locator).text
        self.assertEqual(bun_adaugat, "Bun Test", "Numele bunului adaugat nu este cel asteptat.")
        # self.adaugaretask_page.driver.save_screenshot("Results/test_f_adaugare_task.png")
        # scrie in log ca testul a fost efectuat cu succes
        logger.info("Test adaugare bunuri - Efectuat cu succes. Pentru verificare am adaugat un bun si am verificat daca exista in lista de bunuri")
        time.sleep(1)
        self.adaugarebunuri_page.driver.save_screenshot("Results/test_i_adaugare_bunuri.png")
        time.sleep(1)
        self.adaugarebunuri_page.sterge_active_bunuri()
        time.sleep(2)
        # scrie in log ca testul a fost efectuat cu succes
        logger.info("Test stergere bunuri - Efectuat cu succes.")
        time.sleep(2)

    # @pytest.mark.smoke()  # test smoke
    def test_j_iesire_cont(self):
        '''Metoda care efectueaza testarea paginii de iesire din cont'''
        # Efectuați pașii de deconectare
        self.dashboard_page.iesire_cont()
        time.sleep(1)
        current_url = self.driver.current_url
        self.assertEqual(current_url, "https://app.smart-crm.ro/login", "Nu s-a redirectionat catre pagina de login.")
        # scrie in log ca testul a fost efectuat cu succes
        logger.info("Testare iesire din cont - Iesirea din cont a fost efectuata cu succes. Am verificat daca s-a redirectionat catre pagina de login.")

    def test_k_login_invalid_password(self):
        time.sleep(2)
        '''Metoda care efectueaza testarea paginii de login cu o parola invalida - try - except - else
        '''
        try:
            self.login_page.driver.get("https://app.smart-crm.ro/login")
            # Aceseaza pagina de login si introduce datele de conectare
            self.login_page.enter_username(self.USERNAME)
            time.sleep(2)
            self.login_page.enter_password(self.PAROLA_GRESITA)
            time.sleep(1)
            self.login_page.click_login()
            msg = self.login_page.vreificare_mesaj_parola_gresita()
            # Verifica daca mesajul de eroare este cel asteptat
            self.assertEqual(msg, "Aceste acreditari nu se potrivesc cu mesajul nostru")
            time.sleep(1)
            # Salveaza o captura de ecran a paginii de conectare cu mesajul parola gresita
            self.login_page.driver.save_screenshot("Results/test_j_login_invalid_pass.png")
            time.sleep(2)
        except AssertionError as e:
            # In caz de eroare, scrie in log ca testul a esuat
            logger.error(f"Testare Pagina Login - Test login și returnare mesaj a eșuat: {str(e)}")
            raise  # Ridicare exceptie pentru a fi marcata in raportul de testare
        else:
            # Scrie in log ca testul a fost efectuat cu succes
            logger.info("Testare Pagina Login - Test login și returnare mesaj pentru parola invalida a fost efectuat cu succes.")

    @pytest.mark.skip(reason="Nu mai este necesar")
    def test_titlu_pg_principala(self):
        self.driver.get("https://smart-crm.ro/")
        assert "Smart CRM" in self.driver.title

    # @pytest.mark.smoke()  # test smoke
    def test_smoke_title(self):
        self.test_a_login_valid()
        time.sleep(2)
        assert "Bord" in self.driver.title

if __name__ == '__main__': # rulare test in mod standalone
    unittest.main()