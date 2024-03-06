
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome(service=Service(r'C:\Users\Ashu\Desktop\TOOLS\chromedriver-win64\chromedriver.exe'))
driver.get("https://main.sci.gov.in/judgments")


fromdate_input = driver.find_element(By.CSS_SELECTOR, "#JBJfrom_date")
todate_input = driver.find_element(By.CSS_SELECTOR,"#JBJto_date")

capture = driver.find_element(By.CSS_SELECTOR,"#cap font").text

current_date = driver.find_element(By.CSS_SELECTOR, '#JBJfrom_date').get_property('value')



newfrom_date = "23-08-1996"
newto_date = "23-08-1997"



driver.execute_script(f"arguments[0].setAttribute('value', '{newfrom_date}')", fromdate_input)
driver.execute_script(f"arguments[0].setAttribute('value', '{newto_date}')",todate_input)
driver.find_element(By.CSS_SELECTOR,"#ansCaptcha").send_keys(capture)
element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#v_getJBJ"))
)

element.click()

#

time.sleep(10)