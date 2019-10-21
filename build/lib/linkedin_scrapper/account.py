#import needed object
import time, sys
# from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.ie.options import Options as IeOptions


class Account():
    """Class to connect in you linkedin accouont"""
    def __init__(self, email, password, driver_name):
        """ Constructor for this class """
        self.email = email
        self.password = password
        self.driver_name = driver_name
    
    def connect_chrome_driver(self):
        """Functions to connect with chrome driver """
        #initialise chrome options
        self.options = ChromeOptions()
        #add cookies on driver
        self.options.add_argument("user-data-dir=selenium") 
        #initialise driver
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=self.options)
        return self.driver

    def connect_firefox_driver(self):
        """Functions to connect with firefox driver """
        #initialise chrome options
        self.options = FirefoxOptions()
        #add cookies on driver
        self.options.add_argument("user-data-dir=selenium") 
        #initialise driver
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), firefox_options=self.options)
        return self.driver

    def connect_ie_driver(self):
        """Functions to connect with ie driver """
        #initialise chrome options
        self.options = IeOptions()
        #add cookies on driver
        self.options.add_argument("user-data-dir=selenium") 
        #initialise driver
        self.driver = webdriver.Ie(IEDriverManager().install(), ie_options=self.options)
        return self.driver
    
    def authentification(self):
        #get sign in button, and click 
        self.sign_in_button = self.driver.find_element_by_xpath('//a[@class="nav__button-secondary"]').click()
        #get the email field on login form
        self.email_field = self.driver.find_element_by_id('username')
        #get the password field on login form
        self.password_field = self.driver.find_element_by_id('password')
        #get the login button on login form
        self.login_button = self.driver.find_element_by_xpath('//button[@class="btn__primary--large from__button--floating"]')
        #wait 3 secondes
        time.sleep(1)
        #fill the location field
        self.email_field.clear()
        self.email_field.send_keys(self.email)
        #wait 3 secondes
        time.sleep(1)
        #fill the location field
        self.password_field.clear()
        self.password_field.send_keys(self.password)
        #click on login button
        self.login_button.click()

    def login(self):
        """Function to login in linkedin"""
        #maximize the size of chrome driver
        # chrome_options.add_argument("--start-maximized")
        #create a webdriver object, return the object driver of type selenium.webdriver.chrome.webdriver.WebDriver 
        if self.driver_name == "chrome":  
            try:
                #try to connect with chrome driver
                self.driver = self.connect_chrome_driver()
            except:
                print("Sorry, you can't use chrome driver, please try another driver!")
                sys.exit(0)
        elif self.driver_name == "ie":
            try:
                #try to connect with ie driver
                self.driver = self.connect_ie_driver()
            except:
                print("Sorry, you can't use internet explorer driver, please try another driver!")
                sys.exit(0)
        else:
            try:
                #try to connect with firefox driver
                self.driver = self.connect_firefox_driver()
            except:
                print("sorry, you can't use firefox driver, please try another driver!")
                sys.exit(0)
        #put linkedin url in the driver
        self.driver.get("https://www.linkedin.com")
        #condition to verify if it is the first connection 
        if self.driver.current_url == "https://www.linkedin.com/feed/":
            pass
        else:
            #call the authentification option
            self.authentification()    
        return self.driver