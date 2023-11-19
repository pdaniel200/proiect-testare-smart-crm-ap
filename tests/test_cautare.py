# importare module
import pytest
from pages.pagina_cautare import CautarePagina
from tests.baza_test import PrincipalulTest


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
        self.page.verifica_titlu("DuckDuckGo — ")

    # test pentru efectuarea unei cautari si verificarea rezultatelor
    def test_cautare(self, incarcare_pagina):
        self.page.reazizare_cautare("amazinghouse.ro")

    # test pentru efectuarea unei cautari si verificarea rezultatelor
    # def test_login(self, incarcare_pagina):
        # self.page.reazizare_login("smart-crm.ro")
