from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()

driver.get("https://www.google.com/")

user_input = driver.find_element(by=By.XPATH,value='/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea')
user_input.send_keys('Data Science')
user_input.send_keys(Keys.ENTER)

# link = driver.find_element(by=By.XPATH,value='/html/body/div[6]/div/div[12]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/div/span/a')
# link.click()

wait = WebDriverWait(driver, 10)
link = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/div/div[12]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/div/span/a')))
link.click()

time.sleep(5)


driver.close()

