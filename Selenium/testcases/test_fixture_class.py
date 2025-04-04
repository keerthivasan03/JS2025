import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="class")
def init_driver(request):
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)  # Keeps browser open after test

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.maximize_window()
    request.cls.driver = driver  # Make driver accessible in the test class
    yield
    #driver.quit()


@pytest.mark.usefixtures("init_driver")
class TestBrowser:

    def test_google(self):
        self.driver.get("https://www.google.com")
        print("Opened Google")
        input("Press Enter after checking Google page...") 
    def test_bing(self):
        self.driver.get("https://www.bing.com")
        print("Opened Bing")
