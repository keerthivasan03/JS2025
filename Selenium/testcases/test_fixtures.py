import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver import ActionChains, Keys

# Global driver declaration
driver = None  

@pytest.fixture(scope="function")
def get_driver():
    global driver
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True) 
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
    driver.maximize_window()
    yield driver  # Provide the driver to the test
    driver.quit()  # Close the browser after test execution

def test_example(get_driver):  # Fixture ensures driver initialization
    get_driver.get("https://www.google.com/")
    print("Test executed")

def test_second(get_driver):  # Apply fixture to use the driver
    get_driver.get("https://www.bing.com/")
    print("Second test executed")

