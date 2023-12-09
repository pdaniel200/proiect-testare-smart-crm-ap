# conftest.py
# Fisier cofigurare pytest
import pytest
from Data.configurare_driver import config as configurare

def pytest_addoption(parser):
    """functie utilizata pentru a adauga optiuni personalizate de linie de comanda la pytest in terminal."""
    parser.addoption(
        "--htmlpath",
        action="store",
        default=None,
        help="Specify the path for the HTML report file.",
    )

def pytest_configure(config):
    # Verifica daca o cale htmlpath a fost furnizata ca argument de linie de comanda
    html_report_path = config.getoption("--htmlpath")
    # Daca nu a fost furnizata o cale htmlpath, genereaza un nume de fisier implicit
    if not html_report_path:
        tip_browser = configurare()['browser']
        if configurare()['headless']:
            tip_browser += '_headless'
        default_html_report_path = f"Results/report_test_login_smart_crm_browser_{tip_browser}.html" # Definire nume implicit pentru fisierul html
        config.option.htmlpath = default_html_report_path
    else:
        config.option.htmlpath = html_report_path # Daca deja a fost furnizata o cale htmlpath in linia de comanda, o foloseste

    # Alte configurari pentru pytest (log, markeri)
    config.option.log_level = "INFO"
    config.option.log_format = "%(asctime)s %(levelname)s %(message)s"
    config.option.log_date_format = "%Y-%m-%d %H:%M:%S"
    config.addinivalue_line("markers", "smoke: mark a test as a smoke test") # Adaugare marker pentru smoke test
