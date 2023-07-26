import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions



@pytest.fixture(scope="class")
def setup():
    options = FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    driver.implicitly_wait(5)
    yield driver





