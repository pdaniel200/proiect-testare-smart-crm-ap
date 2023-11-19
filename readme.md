# Testare login si rulare si oprire cronometru, Chrome si Firefox




# Versiune

* Python 3.10

# Rulare

1. Deschide un terminal
2. Accesați directorul rădăcină al proiectului "/proiect-testare-ap/".
3. Creați un mediu virtual: `py -m venv venv`
4. Activați mediul virtual: `.\venv\Scripts\activate`
5. Descărcați bibliotecile necesare:  `pip install -r requirements.txt`

# Executare test

1. Deschide un terminal
2. Din directorul rădăcină al proiectului rulați: `pytest -v --html=results/report.html`

# Alte informații

Optiune de a alege tipul de browser de pe care se face testul
Testele vor fi executate în Chrome dar pot fi modificate în fișierul „/data/config.yaml” pentru a se executa si din Firefox

# Rezultate

Pentru a verifica raportul, deschideți '/results/report.html' odată ce testul s-a încheiat.
   