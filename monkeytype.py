# let's try to automate monkeytype
from selenium import webdriver 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from pynput.keyboard import Key, Controller
import time

chromedriver = "./chromedriver.exe"
keyboard = Controller()

timeout = 10

driver = webdriver.Chrome(chromedriver)

driver.get("https://monkeytype.com/")

element_present = EC.presence_of_element_located((By.ID, "words"))

WebDriverWait(driver, timeout).until(element_present)
time.sleep(2)

# get all the words with class name as 'word'
words = driver.find_elements_by_class_name("word")

# loop through all the words
try:
    for _ in range(500):
        # check for an active class
        active_class = driver.find_element_by_css_selector(".word.active")
        print(active_class.text)

        # keyboard events
        keyboard.type(active_class.text)
        keyboard.press(Key.space)
        keyboard.release(Key.space)
except:
    print('ended')

# it's working, YAY!!!


