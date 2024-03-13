import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager as FirefoxDriverManager


def get_webdriver(browser_name):
    """Возвращает экземпляр веб-драйвера для указанного браузера."""
    if browser_name == "chrome":
        options = ChromeOptions()
        service = ChromeService(ChromeDriverManager().install())
        return webdriver.Chrome(service=service, options=options)
    elif browser_name == "firefox":
        options = FirefoxOptions()
        service = FirefoxService(FirefoxDriverManager().install())
        return webdriver.Firefox(service=service, options=options)
    else:
        raise ValueError("Unsupported browser")


@pytest.fixture()
def selenium(pytestconfig):
    """Фикстура для создания экземпляра веб-драйвера."""
    browser_name = pytestconfig.getini("browser_name")
    selenium_instance = get_webdriver(browser_name)
    yield selenium_instance
    selenium_instance.quit()