from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
#from selenium import * imports all
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as unil
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver import ActionChains, Keys
import time

"""chrome_options = Options()
chrome_options.add_experimental_option("detach", True) 
"""
def get_driver():
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver = get_driver()
driver.get("https://demo.automationtesting.in/Register.html")
driver.maximize_window()
searc=driver.find_element(By.XPATH,"//div/textarea[@ng-model='Adress']")
searc.send_keys("Selenium")
driver.find_element(By.XPATH,"//div//label/input[@value='FeMale']").click()
more=driver.find_elements(By.XPATH,"//div/input[@type='checkbox']")
for fine in more:
    val=fine.get_attribute('value')
    print(val)
    if val=="Cricket":
        fine.click()
select_web= (driver.find_element(By.ID,"Skills"))
sel=Select(select_web)
sel.select_by_value('Configuration')

driver.implicitly_wait(2)

wc=WebDriverWait(driver,4)
#wc.until(unil.element_to_be_selected(By.XPATH,""))
driver.get("https://www.shine.com/myshine/home")

driver.find_element(By.XPATH,"//li[@class='login_mid2 transform1']/input").send_keys("qakeerthivasan@gmail.com")
driver.find_element(By.XPATH,"(//li//input[@aria-label='Email']/parent::li/following-sibling::li/input[@aria-label='Password'])[1]").send_keys("Jobsearch@2024")
driver.find_element(By.XPATH,"//li/div[@class='w-100']/button[normalize-space(text())='Login']").click()
actions= ActionChains(driver)
fd=driver.find_element(By.XPATH," //ul//li//a[normalize-space(text())='Courses']/parent::li/ancestor::ul[@class='navbar_navMenu__LsN0c']")
time.sleep(3)
actions.move_to_element(fd).perform
new_click=driver.find_element(By.XPATH,"//ul//li//ul/li/a[normalize-space(text())='Sales and Marketing']/ancestor::ul[@class='navbar_navMenu__LsN0c']")
time.sleep(3)
actions.click(new_click).key_up(Keys.ENTER).perform()
"""driver.back()
driver.refresh()
driver.forward()
driver.quit()
"""
input("Press Enter to exit...")