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
        self.driver.execute_script("window.open('https://facebook.com')")
        self.driver.execute_script("window.open('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')")
        self.driver.execute_script("window.open('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')")
        self.driver.execute_script("window.open('https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1562200872&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3ded3f1581-e2e4-9895-5d1f-e37405510674&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015')")
        self.driver.execute_script("window.open('https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1562200872&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3ded3f1581-e2e4-9895-5d1f-e37405510674&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015')")
        self.driver.execute_script("window.open('https://www.linkedin.com/uas/login?session_redirect=%2Fvoyager%2FloginRedirect%2Ehtml&fromSignIn=true&trk=uno-reg-join-sign-in')")
        self.driver.execute_script("window.open('https://github.com/login')")
        time.sleep(6)
    
    def loginInformation(self):
        information = [["Messenger Email", "Password"],
                       ["Facebook Email", "Password"], 
                       ["MacEmail", "MacID", "Password"], 
                       ["Gmail", "Passsword"], 
                       ["Hotmail", "Password"], 
                       ["Hotmail", "Password"],
                       ["LinkedIn Email", "Password"],
                       ["Github Username", "Password"]]
        return information
        
    def youTube(self):
        self.driver.switch_to_window(self.driver.window_handles[10])
        time.sleep(3)
        self.driver.find_elements_by_class_name("yt-simple-endpoint style-scope ytd-button-renderer")
    
    def messenger(self, information):
        self.driver.switch_to_window(self.driver.window_handles[8])
        time.sleep(1)
        email = self.driver.find_element_by_id("email")
        email.clear()
        email.send_keys(information[0][0])
        time.sleep(1)
        password = self.driver.find_element_by_id("pass")
        password.clear()
        password.send_keys(information[0][1])
        time.sleep(1)
        loginButton = self.driver.find_element_by_id("loginbutton")
        loginButton.click()
        time.sleep(1)
    
    def facebook(self, information):
        self.driver.switch_to_window(self.driver.window_handles[7])
        email = self.driver.find_element_by_name("email")
        email.clear()
        email.send_keys(information[1][0])
        time.sleep(1)
        password = self.driver.find_element_by_name("pass")
        password.clear()
        password.send_keys(information[1][1])
        time.sleep(1)
        password.submit()
        time.sleep(1)
    
    def gmail(self, information):
        self.driver.switch_to_window(self.driver.window_handles[6])
        emailBar = self.driver.find_element_by_id("identifierId")
        emailBar.clear()
        emailBar.send_keys(information[2][0])
        time.sleep(1)
        nextButton = self.driver.find_element_by_id("identifierNext")
        nextButton.click()
        time.sleep(1)
        macId = self.driver.find_element_by_id("username")
        macId.clear()
        macId.send_keys(information[2][1])
        time.sleep(1)
        macPassword = self.driver.find_element_by_id("password")
        macPassword.clear()
        macPassword.send_keys(information[2][2])
        time.sleep(1)
        submitButton = self.driver.find_element_by_id("submit")
        submitButton.click()
        time.sleep(1)
        acceptButton = self.driver.find_element_by_id("accept")
        acceptButton.click()
        time.sleep(1)
        submitButton2 = self.driver.find_element_by_name("_eventId_proceed")
        submitButton2.click()
        time.sleep(1)
    
    def gmail2(self, information):
        self.driver.switch_to_window(self.driver.window_handles[5])
        emailBar = self.driver.find_element_by_id("identifierId")
        emailBar.clear()
        emailBar.send_keys(information[3][0])
        time.sleep(1)
        nextButton = self.driver.find_element_by_id("identifierNext")
        nextButton.click()
        time.sleep(1)
        passwordBar = self.driver.find_element_by_name("password")
        passwordBar.clear()
        passwordBar.send_keys(information[3][1])
        time.sleep(1)
        nextButton = self.driver.find_element_by_id("passwordNext")
        nextButton.click()
        time.sleep(1)
    
    def hotmail1(self, information):
        self.driver.switch_to_window(self.driver.window_handles[4])
        emailBar = self.driver.find_element_by_id("i0116")
        emailBar.clear()
        emailBar.send_keys(information[4][0])
        time.sleep(1)
        nextButton = self.driver.find_element_by_id("idSIButton9")
        nextButton.click()
        time.sleep(1)
        passwordBar = self.driver.find_element_by_id("i0118")
        passwordBar.clear()
        time.sleep(1)
        passwordBar.send_keys(information[4][1])
        time.sleep(1)
        nextButton = self.driver.find_element_by_id("idSIButton9")
        nextButton.click()
        time.sleep(2)
        passwordBar = self.driver.find_element_by_id("i0118")
        passwordBar.clear()
        time.sleep(1)
        passwordBar.send_keys(information[4][1])
        time.sleep(1)
        nextButton = self.driver.find_element_by_id("idSIButton9")
        nextButton.click()
        time.sleep(2)
    

    def hotmail2(self, information):
        self.driver.switch_to_window(self.driver.window_handles[3])
        emailBar = self.driver.find_element_by_id("i0116")
        emailBar.clear()
        emailBar.send_keys(information[5][0])
        time.sleep(1)
        nextButton = self.driver.find_element_by_id("idSIButton9")
        nextButton.click()
        time.sleep(1)
        passwordBar = self.driver.find_element_by_id("i0118")
        passwordBar.clear()
        passwordBar.send_keys(information[5][1])
        time.sleep(1)
        nextButton = self.driver.find_element_by_id("idSIButton9")
        nextButton.click()
        time.sleep(1)
    

    def linkedIn(self, information):
        self.driver.switch_to_window(self.driver.window_handles[2])
        email = self.driver.find_element_by_id("username")
        email.clear()
        email.send_keys(information[6][0])
        time.sleep(1)
        password = self.driver.find_element_by_id("password")
        password.clear()
        password.send_keys(information[6][1])
        password.submit()
        time.sleep(3)
        self.driver.execute_script("window.open('https://www.linkedin.com/feed/')")
        time.sleep(3)
        self.driver.switch_to_window(self.driver.window_handles[2])
        self.driver.close()
    

    def github(self, information):
        self.driver.switch_to_window(self.driver.window_handles[1])
        username = self.driver.find_element_by_id("login_field")
        username.clear()
        username.send_keys(information[7][0])
        time.sleep(1)
        password = self.driver.find_element_by_id("password")
        password.clear()
        password.send_keys(information[7][1])
        time.sleep(1)
        nextButton = self.driver.find_element_by_name("password")
        nextButton.click()
        time.sleep(1)


    def executeAutomation(self):
        self.setupSelenium()
        self.openTabs()
        information = self.loginInformation()
        self.messenger(information)
        self.facebook(information)
        self.gmail(information)
        self.gmail2(information)
        self.hotmail1(information)
        self.hotmail2(information)
        self.linkedIn(information)
        self.github(information)
        
        

if __name__ == "__main__":
    login = AutomatedLogins()
    login.executeAutomation()
