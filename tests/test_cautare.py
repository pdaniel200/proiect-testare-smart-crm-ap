# importare module
import pytest
from pages.pagina_cautare import CautarePagina
from tests.baza_test import PrincipalulTest
from selenium.webdriver.common.keys import Keys



# definire clasa TesteazaCautare, care moșteneste functii din clasa PrincipalulTest
class TesteazaCautare(PrincipalulTest):

    # decorator Pytest care incarca paginile necesare inaintea testului
    @pytest.fixture
    def incarcare_pagina(self):
        # initializare si navigare la pagina de cautare
        self.page = CautarePagina(self.driver, self.wait)
        self.page.mergi_la_cautare_pagina()

    # test pentru verificarea titlului paginii de cautare
    def test_titlu(self, incarcare_pagina):
        self.page.verifica_titlu("Smart CRM")

    # test pentru efectuarea de login si pornire oprire cronometru

    def test_login(self, incarcare_pagina):
        # Deschide pagina principala
        self.page.reazizare_login("https://smart-crm.ro/")
