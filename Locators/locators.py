''' fisier cu locatori pentru aplicatia Smart CRM
'''

class LocatoriPaginaSmartCrm():

    #locatori pagina de login
    USERNAME_TEXTBOX_ID = "email"
    PASSWORD_TEXTBOX_ID = "password"
    BUTON_INAINTE_ID = "submit-next"
    LOGIN_BUTON_ID = "submit-login"
    MESAJ_INVALID_FEEDBACK_XPATH = "//div[@class='invalid-feedback']"

    #locatori pagina de sarcini
    PORNIRE_CRONOMETRU_XPATH = "//i[@class='bi bi-play-circle-fill']"
    OPRIRE_CRONOMETRU_XPATH = "//i[@class='bi bi-stop-circle-fill']"

    #locatori pagina adaugare cont bancar
    BUTON_FINANTE_XPATH = "//span[contains(text(),'FINANȚE')]"
    BUTON_CONTURI_BANCARE_XPATH = "//a[normalize-space()='Conturi bancare']"
    BUTON_ADAUGARE_CONT_BANCAR_XPATH = "//a[@class='btn btn-primary rounded f-14 p-2 mr-3 openRightModal float-left']"
    BUTON_SELECTARE_TIP_CONT_XPATH = "//label[@for='type-cash']"
    CAMP_NUME_DETINATOR_CONT_ID = "account_name"
    CAMP_NUMAR_CONTACT_ID = "contact_number"
    CAMP_SOLD_DESCHIDERE_ID = "opening_balance"
    SELECTOR_STARE_CONT_XPATH = "//div[contains(text(),'--')]"
    SELECTOR_STARE_CONT_ACTIV_XPATH = "/html/body/div[6]/div/div/div/div/form/div/div[1]/div[9]/div/div/div/div[2]/ul/li[2]/a/span"
    BUTON_ADAUGARE_CONT_XPATH = "save-bankaccount"
    BUTON_ACTIUNE_CONT_XPATH = "/html/body/div[1]/section/div[4]/div[2]/div/div[1]/div/table/tbody/tr[1]/td[8]/div/div/a"
    BUTON_STERGE_CONT_XPATH = "/html/body/div[1]/section/div[4]/div[2]/div/div[1]/div/table/tbody/tr[1]/td[8]/div/div/div/a[3]"
    BUTON_CONFIRMARE_STERGERE_CONT_XPATH = "/html/body/div[7]/div/div[3]/button[1]"

    #locatori transfer intre conturi
    NUME_DETINATOR_CONT_XPATH = "//a[normalize-space()='cont 1 companie']"
    BUTON_TRANSFER_CSS = ".btn.btn-secondary.rounded.f-14.p-2.openRightModal[href='https://app.smart-crm.ro/account/bankaccount/create-transaction?accountId=8&type=account']"
    SELECTOR_IN_CONTUL_XPATH = "//div[@class='filter-option-inner-inner']"
    SELECTOR_CONT2COMPANIE_XPATH = "/html[1]/body[1]/div[6]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[2]/a[1]/span[1]"
    CAMP_CANTITATE_ID = "amount"
    BUTON_SALVARE_XPATH = "//button[@id='save-transaction']"

    #locatori alocare si stergere program angajat
    BUTON_MENIU_HR_XPATH = "//span[normalize-space()='HR']"
    BUTON_MENIU_ALOCARE_PROGRAM_CSS = "a[title='Alocă Program Angajați']"
    BUTON_PRIMA_ZI_XPATH = "//tbody/tr/td[2]/button[1]//*[name()='svg']"
    BUTON_PRIMA_ZI_ALOCATA_XPATH = "/html/body/div[1]/section/div[4]/div[2]/div/div/div/div[2]/table/tbody/tr/td[2]/button/div/div/div"
    SELECTOR_TIP_PROGGRAM_XPATH = "/html/body/div[2]/div/div/div[2]/form/div/div[3]/div/div/button"
    SELECTOR_PROGRAM_LUCRU_XPATH = '//*[@id="bs-select-4-1"]/span'
    BUTON_SALVARE_PROGRAM_XPATH = "/html/body/div[2]/div/div/div[3]/button"
    BUTON_STERGE_PROGRAM_XPATH = "/html/body/div[2]/div/div/div[3]/button[1]"

    #locatori adaugare si stergere task
    BUTON_ADAUGARE_SARCINA_XPATH = "//a[@class='btn btn-primary rounded f-14 p-2 mr-3 openRightModal float-left']"
    CAMP_TITLU_SARCINA_ID = "heading"
    CHECKBOX_FARA_DATA_SCADENTA_XPATH = '//*[@id="without_duedate"]'
    SELECTOR_ATRIBUIRE_XPATH = "/html/body/div[6]/div/div/div/div/form/div/div[1]/div[9]/div/div/div[1]/button/div/div/div"
    SELECTEAZA_ATRIBUIRE_UTILIZATOR_XPATH = "//span[@class='text']"
    BUTON_SALVARE_TASK_ID = "save-task-form"
    BUTON_ACTIUNE_LA_TASK_XPATH = "/html/body/div[1]/section/div[4]/div[2]/div/div[1]/div/table/tbody/tr[1]/td[11]/div/div/a/i"
    BUTON_STERGE_TASK_XPATH = "/html/body/div[1]/section/div[4]/div[2]/div/div[1]/div/table/tbody/tr[1]/td[11]/div/div/div/a[3]"
    BUTON_CONFIRMARE_STERGERE_TASK_XPATH = "/html/body/div[8]/div/div[3]/button[1]"

    #locatori adaugare stergere comanda furnizor
    BUTON_MENIU_ACHIZITII_XPATH = "//span[contains(text(),'Achiziții și Furnizori')]"
    BUTON_MENIU_COMENZI_FURNIZORI_XPATH = "//a[contains(text(),'Comenzi')]"
    BUTON_ADAUGARE_COMANDA_XPATH = "//a[@class='btn btn-primary rounded f-14 p-2 mr-3 float-left openRightModal']"
    SELECTOR_FURNIZOR_XPATH = "/html/body/div[6]/div/div/div/form/div[1]/div[2]/div/div/div/button"
    SELECTEAZA_FURNIZOR_1_XPATH = "/html/body/div[6]/div/div/div/form/div[1]/div[2]/div/div/div/div/div/ul/li[2]/a"
    SELECTOR_PRODUS_XPATH = "/html/body/div[6]/div/div/div/form/div[2]/div[2]/div/div/div[1]/button/div/div/div"
    SELECTEAZA_SERVICIU_1_XPATH = "/html/body/div[6]/div/div/div/form/div[2]/div[2]/div/div/div[1]/div/div[2]/ul/li[2]/a"
    CAMP_CANTITATE_PRODUS_XPATH = '//*[@id="sortable"]/div/div/table/tbody/tr[2]/td[3]/input[1]'
    BUTON_SALVARE_COMANDA_XPATH = '//*[@id="saveOrderForm"]/div[8]/div/div/button'
    BUTON_SALVARE_SI_MARCARE_TRIMISA_XPATH = '//*[@id="saveOrderForm"]/div[8]/div/div/ul/li[3]/a'
    BUTON_ACTIUNE_COMANDA_XPATH = "/html/body/div[1]/section/div[4]/div[2]/div/div[1]/div/table/tbody/tr[1]/td[7]/div/div/a"
    BUTON_STERGE_COMANDA_XPATH = "/html/body/div[1]/section/div[4]/div[2]/div/div[1]/div/table/tbody/tr[1]/td[7]/div/div/div/a[8]"
    BUTON_CONFIRMARE_STERGERE_COMANDA_XPATH = '//*[@id="body"]/div[8]/div/div[3]/button[1]'

    #locatori adaugare stergere cheltuiala
    BUTON_MENIU_CHELTUIELI_XPATH = "//a[@title='Cheltuieli']"
    BUTON_ADAUGARE_CHELTUIALA_XPATH = "//a[@class='btn btn-primary rounded f-14 p-2 mr-3 float-left openRightModal']"
    CAMP_NUME_ARTICOL_CHELTUIALA_ID = "item_name"
    CAMP_PRET_CHELTUIALA_ID = "price"
    SELECTOR_ANGAJAT_XPATH = '//*[@id="save-expense-data-form"]/div/div[1]/div[6]/div/div/button'
    SELECTEAZA_ANGAJAT_1_XPATH = '/html/body/div[6]/div/div/div/div/form/div/div[1]/div[6]/div/div/div/div[2]/ul/li[2]/a'
    BUTON_SALVARE_CHELTUIALA_XPATH = "//button[@id='save-expense-form']"
    BUTON_ACTIUNE_CHELTUIALA_XPATH = "/html/body/div[1]/section/div[4]/div[2]/div/div[1]/div/table/tbody/tr[1]/td[9]/div/div/a"
    BUTON_STERGE_CHELTUIALA_XPATH = "/html/body/div[1]/section/div[4]/div[2]/div/div[1]/div/table/tbody/tr[1]/td[9]/div/div/div/a[3]"
    BUTON_CONFIRMARE_STERGERE_CHELTUIALA_XPATH = '//*[@id="body"]/div[8]/div/div[3]/button[1]'

    #locatori adaugare stergere bunuri
    BUTON_MENIU_ACHIZITII_BUNURI_XPATH = "//span[normalize-space()='Active | Bunuri']"
    BUTON_ADAUGARE_ACTIVE_XPATH = '//*[@id="table-actions"]/a'
    CAMP_DENUMIRE_BUN_ID = "name"
    SELECTOR_TIP_ACTIVE_XPATH = '//*[@id="save-asset-form"]/div/div[1]/div[1]/div/div[2]/div/div[1]/button'
    SELECTEAZA_TIP_ACTIVE_XPATH = "//span[normalize-space()='scule si unelte']"
    CAMP_NUMAR_SERIE_ACTIVE_ID = "serial_number"
    BUTON_SALVEAZA_ACTIVE_XPATH = "//button[@id='save-asset']"
    BUTON_ACTIUNE_ACTIVE_BUNURI_XPATH = "/html/body/div[1]/section/div[4]/div[2]/div/div[1]/div/table/tbody/tr[1]/td[7]/div/div/a/i"
    BUTON_STERGE_ACTIVE_BUNURI_XPATH = '/html/body/div[1]/section/div[4]/div[2]/div/div[1]/div/table/tbody/tr[1]/td[7]/div/div/div/a[4]'
    BUTON_CONFIRMARE_STERGERE_ACTIVE_BUNURI_XPATH = '//*[@id="body"]/div[7]/div/div[3]/button[1]'

    #locatori pagina de logout
    BUTON_LOGOUT_XPATH = "//a[@class='d-block header-icon-box']//*[name()='svg']//*[name()='path' and contains(@fill,'currentCol')]"
    # BUTON_LOGOUT = (By.XPATH, "//a[@class='d-block header-icon-box']//*[name()='svg']//*[name()='path' and contains(@fill,'currentCol')]")