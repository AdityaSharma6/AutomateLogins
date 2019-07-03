from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()



driver.get("https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1561935703&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3d8f0fb082-a959-5f98-92de-950095e9b5f0&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015")
time.sleep(1)

signInBar = driver.find_element_by_name("loginfmt")
signInBar.clear()
signInBar.send_keys("ENTER YOUR VALUE")
time.sleep(1)

nextButton = driver.find_element_by_id("idSIButton9")
nextButton.click()
time.sleep(0.75)

passwordBar = driver.find_element_by_id("i0118")
passwordBar.clear()
passwordBar.send_keys("ENTER YOUR VALUE")
time.sleep(0.75)

signInButton = driver.find_element_by_id("idSIButton9")
signInButton.click()
time.sleep(0.75)

driver.execute_script("window.open('https://gmail.com', 'new window')")
driver.switch_to_window(driver.window_handles[1])
time.sleep(1)