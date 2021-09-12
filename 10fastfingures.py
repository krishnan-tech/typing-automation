# now let's automate 10fastfingures website :)

from selenium import webdriver 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

chromedriver = "./chromedriver.exe"
timeout = 10

driver = webdriver.Chrome(chromedriver)
driver.get("https://10fastfingers.com/typing-test/english")

# wait till the inputfield is available
WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.ID, "inputfield")))
time.sleep(3)

# if there is cookie model then click allow all cookies
cookie_model = driver.find_element_by_id("CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll").click()

# input field
input_field = driver.find_element_by_id("inputfield")
time.sleep(1)

for _ in range(500):
    highlighted_class = driver.find_element_by_class_name("highlight")
    print(highlighted_class.text)
    input_field.send_keys(highlighted_class.text + " ")


# it is working, yay!!!!



