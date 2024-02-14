from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    element = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button = browser.find_element(By.CSS_SELECTOR, "#book").click()
    x_form = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    x = calc(x_form)
    browser.find_element(By.CSS_SELECTOR, "input.form-control").send_keys(x)
    button = browser.find_element(By.CSS_SELECTOR, "button#solve").click()
finally:
    time.sleep(10)
    browser.quit()