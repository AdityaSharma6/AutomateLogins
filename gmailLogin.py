'''from AutomateLogins import loginAutomation
gmailLogin = loginAutomation()
gmailLogin.executeGmail()'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://google.com")
driver.execute_script("window.open('https://youtube.com', 'new window')")
driver.execute_script("window.open('https://messenger.com', 'new window')")
driver.execute_script("window.open('https://gmail.com', 'new window')")
