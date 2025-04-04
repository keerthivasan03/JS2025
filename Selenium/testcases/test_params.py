import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture(scope="function", params=["chrome", "firefox"])
def get_driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif request.param == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    
    driver.maximize_window()
    yield driver
    driver.quit()  # Closes the browser after each test

def test_google(get_driver):
    get_driver.get("https://www.google.com")
    print(f"Test ran on {get_driver.name}")  # Identifies browser

def test_bing(get_driver):
    get_driver.get("https://www.bing.com")
    print(f"Test ran on {get_driver.name}")
