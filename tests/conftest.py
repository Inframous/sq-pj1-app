import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture(scope="class")
def setup():
    options = FirefoxOptions()
    options.add_argument("--headless")
    # driver = webdriver.Firefox(options=options)
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.implicitly_wait(5)
    yield driver





