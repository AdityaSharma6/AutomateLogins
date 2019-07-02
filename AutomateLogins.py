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
signInBar.send_keys("Aditya_Sharma_@hotmail.com")
time.sleep(1)

nextButton = driver.find_element_by_id("idSIButton9")
nextButton.click()
time.sleep(0.75)

passwordBar = driver.find_element_by_id("i0118")
passwordBar.clear()
passwordBar.send_keys("PASSWORD")
time.sleep(0.75)

signInButton = driver.find_element_by_id("idSIButton9")
signInButton.click()
time.sleep(0.75)

driver.execute_script("window.open('https://gmail.com', 'new window')")
driver.switch_to_window(driver.window_handles[1])
time.sleep(1)
        
emailBar = driver.find_element_by_id("identifierId")
emailBar.clear()
emailBar.send_keys("EMAIL@mcmaster.ca")
time.sleep(1)

nextButton = driver.find_element_by_id("identifierNext")
nextButton.click()
time.sleep(2)

driver.switch_to_window(driver.window_handles[1])
macId = driver.find_element_by_id("username")
macId.clear()
macId.send_keys("USERID")
time.sleep(1)

macPassword = driver.find_element_by_id("password")
macPassword.clear()
macPassword.send_keys("PASSWORD")
time.sleep(1)

submitButton = driver.find_element_by_id("submit")
submitButton.click()

acceptButton = driver.find_element_by_id("accept")
acceptButton.click()

submitButton2 = driver.find_element_by_name("_eventId_proceed")
submitButton2.click()



'''
class loginAutomation():
    def __init__(self):
        self.driver = None
    
    def setupSelenium(self):
        self.driver = webdriver.Chrome()
    #driver.execute_script("window.open('https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1561935703&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3d8f0fb082-a959-5f98-92de-950095e9b5f0&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015', 'new window')")

    def hotmailLogin(self):
        self.driver.get("https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1561935703&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3d8f0fb082-a959-5f98-92de-950095e9b5f0&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015")
        time.sleep(1)

        signInBar = self.driver.find_element_by_name("loginfmt")
        signInBar.clear()
        signInBar.send_keys("Aditya_Sharma_@hotmail.com")
        time.sleep(1)

        nextButton = self.driver.find_element_by_id("idSIButton9")
        nextButton.click()
        time.sleep(0.75)

        passwordBar = self.driver.find_element_by_id("i0118")
        passwordBar.clear()
        passwordBar.send_keys("PASSWORD")
        time.sleep(0.75)

        signInButton = self.driver.find_element_by_id("idSIButton9")
        signInButton.click()
        time.sleep(0.75)
        
    def gmailLogin(self):
        self.driver.get("https://gmail.com")
        time.sleep(1)
        
        emailBar = self.driver.find_element_by_id("identifierId")
        emailBar.clear()
        emailBar.send_keys("USERID@mcmaster.ca")
        time.sleep(1)

        nextButton = self.driver.find_element_by_id("identifierNext")
        nextButton.click()

        macId = self.driver.find_element_by_id("username")
        macId.clear()
        macId.send_keys("USERID")
        time.sleep(1)

        macPassword = self.driver.find_element_by_id("password")
        macPassword.clear()
        macPassword.send_keys("PASSWORD")
        time.sleep(1)

        submitButton = self.driver.find_element_by_id("submit")
        submitButton.click()
    
    def mcmasterLogin(self):
        self.driver.get("https://epprd.mcmaster.ca/psp/prepprd/?cmd=login")
        

    def executeHotmail(self):
        self.setupSelenium()
        self.hotmailLogin()
        self.gmailLogin()
    
    def executeGmail(self):
        self.setupSelenium()
        self.gmailLogin()


if __name__ == "__main__":
    automate = loginAutomation()
    automate.executeHotmail()
    '''
