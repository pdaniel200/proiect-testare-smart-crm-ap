# definire clasa PaginaDeBaza
class PaginaDeBaza:

    # Constructorul clasei, se initializeaza un driver selenium si asteptarea
    def __init__(self, driver, wait):
        self.driver = driver  # atribuire obiectul driver
        self.wait = wait  # atribuire asteptare

    # Navigare la pagina din URL din clasa CautarePagina
    def mergi_la_pagina(self, url):
        self.driver.get(url)

    # Metoda de a prelua titlul paginii curente
    def preluare_titlu(self):
        return self.driver.title
