from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class AutomatedLogins():
    def __init__(self):
        self.driver = None
    
    def setupSelenium(self):
        self.driver = webdriver.Chrome()
    
    def openTabs(self):
        self.driver.get("https://google.com")
        self.driver.execute_script("window.open('https://youtube.com')")
        self.driver.execute_script("window.open('https://messenger.com')")
        self.driver.execute_script("window.open('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')")
        self.driver.execute_script("window.open('https://www.linkedin.com/uas/login?session_redirect=%2Fvoyager%2FloginRedirect%2Ehtml&fromSignIn=true&trk=uno-reg-join-sign-in')")
        self.driver.execute_script("window.open('https://facebook.com')")
        self.driver.execute_script("window.open('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')")

        time.sleep(5)
        
    
    def youTube(self):
        self.driver.switch_to_window(self.driver.window_handles[6])
        time.sleep(3)
        self.driver.find_elements_by_class_name("yt-simple-endpoint style-scope ytd-button-renderer")
    
    def messenger(self):
        self.driver.switch_to_window(self.driver.window_handles[5])
        time.sleep(1)
        email = self.driver.find_element_by_id("email")
        email.clear()
        email.send_keys("ENTER YOUR VALUE")
        time.sleep(1)
        password = self.driver.find_element_by_id("pass")
        password.clear()
        password.send_keys("ENTER YOUR VALUE")
        loginButton = self.driver.find_element_by_id("loginbutton")
        loginButton.click()
        time.sleep(1)

    
    def gmail(self):
        self.driver.switch_to_window(self.driver.window_handles[4])
        emailBar = self.driver.find_element_by_id("identifierId")
        emailBar.clear()
        emailBar.send_keys("ENTER YOUR VALUE")
        time.sleep(1)
        nextButton = self.driver.find_element_by_id("identifierNext")
        nextButton.click()
        time.sleep(1)
        macId = self.driver.find_element_by_id("username")
        macId.clear()
        macId.send_keys("ENTER YOUR VALUE")
        time.sleep(1)
        macPassword = self.driver.find_element_by_id("password")
        macPassword.clear()
        macPassword.send_keys("ENTER YOUR VALUE")
        time.sleep(1)
        submitButton = self.driver.find_element_by_id("submit")
        submitButton.click()
        acceptButton = self.driver.find_element_by_id("accept")
        acceptButton.click()
        submitButton2 = self.driver.find_element_by_name("_eventId_proceed")
        submitButton2.click()
        time.sleep(1)

        #self.driver.find_element_by_id("identifierId").clear().send_keys("Aditya_Sharma_@hotmail.com").submit()
    
    def linkedIn(self):
        self.driver.switch_to_window(self.driver.window_handles[3])
        email = self.driver.find_element_by_id("username")
        email.clear()
        email.send_keys("ENTER YOUR VALUE")
        time.sleep(1)
        password = self.driver.find_element_by_id("password")
        password.clear()
        password.send_keys("ENTER YOUR VALUE")
        password.submit()
        time.sleep(3)
        self.driver.execute_script("window.open('https://www.linkedin.com/feed/')")
        time.sleep(3)
        self.driver.switch_to_window(self.driver.window_handles[3])
        self.driver.close()
    
    def facebook(self):
        self.driver.switch_to_window(self.driver.window_handles[2])
        email = self.driver.find_element_by_name("email")
        email.clear()
        email.send_keys("ENTER YOUR VALUE")
        time.sleep(1)
        password = self.driver.find_element_by_name("pass")
        password.clear()
        password.send_keys("ENTER YOUR VALUE")
        time.sleep(1)
        password.submit()
    
    def gmail2(self):
        self.driver.switch_to_window(self.driver.window_handles[1])
        emailBar = self.driver.find_element_by_id("identifierId")
        emailBar.clear()
        emailBar.send_keys("ENTER YOUR VALUE")
        time.sleep(1)
        nextButton = self.driver.find_element_by_id("identifierNext")
        nextButton.click()
        time.sleep(2)
        passwordBar = self.driver.find_element_by_id("password")
        passwordBar.clear()
        passwordBar.send_keys("ENTER YOUR VALUE")
        time.sleep(1)
        passwordBar.submit()

    def executeAutomation(self):
        self.setupSelenium()
        self.openTabs()
        self.messenger()
        self.gmail()
        self.linkedIn()
        self.facebook()
        self.gmail2()
        #array = [self.openTabs(), self.openTabs() ]
        #for i in range(2):
        #    array[i]

if __name__ == "__main__":
    login = AutomatedLogins()
    login.executeAutomation()