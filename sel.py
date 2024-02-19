from selenium import webdriver

def get_drvier():
  # Set options to make browsing easier
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")

  driver = webdriver.Chrome(options=options)
  driver.get("https://www.pythonanywhere.com/login/")
  return driver

def main():
  driver = get_drvier()
  driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[1]").send_keys("automate")


print(main())