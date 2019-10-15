#import needed object
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

class Account():

    def __init__(self, email, password):
        """ Constructor for this class """

        self.email = email
        self.password = password
    
    def authentification(self):
        #get sign in button, and click 
        self.signInButton = self.driver.find_element_by_xpath('//a[@class="nav__button-secondary"]').click()
        #get the email field on login form
        self.emailField = self.driver.find_element_by_id('username')
        #get the password field on login form
        self.passwordField = self.driver.find_element_by_id('password')
        #get the login button on login form
        self.loginButton = self.driver.find_element_by_xpath('//button[@class="btn__primary--large from__button--floating"]')

        #wait 3 secondes
        time.sleep(1)
        #fill the location field
        self.emailField.clear()
        self.emailField.send_keys(self.email)

        #wait 3 secondes
        time.sleep(1)
        #fill the location field
        self.passwordField.clear()
        self.passwordField.send_keys(self.password)


        #click on login button
        self.loginButton.click()

    def login(self):
        """
        Function to login in linkedin
        """
        
        #initialise chrome options
        chrome_options = Options()
        #add cookies on driver
        chrome_options.add_argument("user-data-dir=selenium") 
        #maximize the size of chrome driver
        # chrome_options.add_argument("--start-maximized")
        #create a webdriver object, return the object driver of type selenium.webdriver.chrome.webdriver.WebDriver
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
        #put linkedin url in the driver
        self.driver.get("https://www.linkedin.com")
        #condition to verify if it is the first connection 
        if self.driver.current_url == "https://www.linkedin.com/feed/" :
            pass
        else :
            #call the authentification option
            self.authentification()
    
        return self.driver