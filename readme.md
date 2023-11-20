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

# Se poate alege un tip de browswer chrome/firefox pentru efectuarea testului
1. browser: chrome
2. browser: firefox

Testele vor fi executate în Chrome dar pot fi modificate în fișierul „/data/config.yaml” pentru a se executa si din Firefox

# Vizibilitate browser la rularea testului True/False
1. headless: False
2. headless: True

# Rezultate

Pentru a verifica raportul, deschideți '/results/report.html' odată ce testul s-a încheiat.

# Se fac screenshoturi la fiecare pas major

Pentru a verifica raportul, deschideți '/results/
