import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.mark.usefixtures("setup")
class TestService():
    def test_greeting(self, setup):
        driver = setup
        driver.get("http://localhost:80/")

        # Enter the first username
        username_input = driver.find_element(By.ID, 'username')
        username_input.send_keys("test_user1")
        username_input.send_keys(Keys.RETURN)

        assert "test_user1" in driver.page_source

        # Go back to the form and enter the second username
        driver.get("http://localhost:80/sayhello")
        username_input = driver.find_element(By.ID, "username")
        username_input.send_keys("test_user2")
        username_input.send_keys(Keys.RETURN)

        assert "test_user2" in driver.page_source

        # Quit the driver and stop the app thread
        driver.quit()


@pytest.mark.usefixtures("setup")
class TestDatabase():
    def test_database(self, setup):
        driver = setup

        # Check if both users are listed in the database view
        driver.get("http://localhost:80/db")
        assert "test_user1" in driver.page_source
        assert "test_user2" in driver.page_source

        # Quit the driver and stop the app thread
        driver.quit()
