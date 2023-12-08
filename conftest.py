'''
fisierul conftest.py este un fisier de configurare pentru pytest
Acest fisier este incarcat automat de pytest inainte de executarea testelor.
'''


# conftest.py

def pytest_configure(config):
    config.option.log_level = "INFO"
    config.option.log_format = "%(asctime)s %(levelname)s %(message)s"
    config.option.log_date_format = "%Y-%m-%d %H:%M:%S"
    config.addinivalue_line("markers", "smoke: mark a test as a smoke test")
