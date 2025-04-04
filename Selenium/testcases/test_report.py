import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="class")
def get_driver():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()

@allure.severity(allure.severity_level.CRITICAL)
class TestWebAutomation:
    
    @allure.title("Test Google Home Page")
    def test_google(self, get_driver):
        with allure.step("Opening Google Homepage"):
            get_driver.get("https://www.google.com")
        with allure.step("Verifying Page Title"):
            assert "Google" in get_driver.title

    @allure.title("Test Bing Home Page")
    def test_bing(self, get_driver):
        with allure.step("Opening Bing Homepage"):
            get_driver.get("https://www.bing.com")
        with allure.step("Verifying Page Title"):
            assert "Bing" in get_driver.title
