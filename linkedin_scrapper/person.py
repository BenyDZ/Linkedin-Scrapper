#import needed object
import time
from .functions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Person():
    def __init__(self, driver):
        """ Constructor for this class """
        #initialise needed object
        self.driver = driver

    def search_by_name_and_key_word(self, full_name, keyword=""):
        """Function to search a person in linkedin by her name and the a key word like company name, 
        take driver, the full name and the domain name on the company where he work"""
        #initialise the keyword
        keyword = keyword
        #get the search bar
        search_bar = self.driver.find_element_by_class_name(
            'search-global-typeahead__input')
        #clear search bar
        search_bar.clear()
        #fill search bar
        search_bar.send_keys(full_name + " " + keyword)
        #wait 1 seconde
        time.sleep(2)
        #click on Enter button
        search_bar.send_keys(u'\ue007')
        if keyword != "":
            #wait 2 secondes
            time.sleep(5)
            #get and click on person links
            driver.find_elements_by_tag_name('h3')[-1].click()
        else:
            #wait 5 secondes
            time.sleep(5)
            search_result = driver.find_elements_by_tag_name('h3')
            #check if search result is upper than 2
            if len(search_result) > 2:
                #click on the first result
                search_result[1].click()
            
    def search_by_account_link(self, account_link):
        """Function to search a person by her """
        #open accoubt link in the driver
        account_link = account_link
        self.driver.get(account_link)

    def get_experiences(self):
        """ function to get experiences datas """
        #scroll until the midlle of the page
        self.driver.execute_script("window.scrollTo(0, Math.ceil(document.body.scrollHeight/2));")
        #wait until presence on the experience section
        experience_section = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.ID, "experience-section")))
        try:
            #click on button see more
            see_more_button = self.driver.find_element_by_xpath(
                '//button[@class="pv-profile-section__see-more-inline pv-profile-section__text-truncate-toggle link link-without-hover-state"]').click()
        except:
            pass

        #get all job_titles datas
        job_titles = self.driver.find_elements_by_xpath(
            '//h3[@class="t-16 t-black t-bold"]')
        #get all company_names
        company_names = self.driver.find_elements_by_xpath(
            '//p[@class="pv-entity__secondary-title t-14 t-black t-normal"]')
        experiences = []
        #browse all company name and job titles in same times
        for job_title, company_name in zip(job_titles, company_names):
            #add job titles and companies names in the list experiences
            experiences.append(job_title.text + ", " + company_name.text)       
        return experiences
    
    def get_training(self):
        """Function to get all trainings datas"""
        #scroll until the midlle of the page
        self.driver.execute_script("window.scrollTo(0, Math.ceil(document.body.scrollHeight/2));")
        #wait until presence on the education section
        education_section = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
            (By.ID, "education-section")))
        #get all school trainings name
        school_names = self.driver.find_elements_by_xpath(
            '//h3[@class="pv-entity__school-name t-16 t-black t-bold"]')
        #get all degrees title
        degrees = self.driver.find_elements_by_xpath(
            '//p[@class="pv-entity__secondary-title pv-entity__degree-name t-14 t-black t-normal"]//span[@class="pv-entity__comma-item"]')
        #get all trainings domain
        domains = self.driver.find_elements_by_xpath(
            '//p[@class="pv-entity__secondary-title pv-entity__fos t-14 t-black t-normal"]//span[@class="pv-entity__comma-item"]')
        trainig = []
        #browse all school_names, degrees, domain in the same time
        for school_name, degree, domain in zip(school_names, degrees, domains):
            trainig.append(school_name.text + ", " + degree.text + ", " + domain.text)
        return trainig
    
    def get_skills(self):
        """Function to get all skills datas"""
        #scroll until the midlle of the page
        self.driver.execute_script("window.scrollTo(0, Math.ceil(document.body.scrollHeight/2));")
        #wait until presence on the education section
        education_section = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
            (By.ID, "education-section")))
        #get all skills
        time.sleep(1)
        skills_names = self.driver.find_elements_by_xpath(
            '//ol[@class="pv-skill-categories-section__top-skills pv-profile-section__section-info section-info pb1"]/li/div/div/p')    
        skills = []
        #browse all skills
        for skill in skills_names:
            skills.append(skill.text)     
        return skills

    def get_knowledges_tools(self):
        """ Function to get all Knowledges datas """
        #scroll until the midlle of the page
        self.driver.execute_script("window.scrollTo(0, Math.ceil(document.body.scrollHeight/2));")
        #wait until presence on the education section
        education_section = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
            (By.ID, "education-section")))
        try:
            #click on the see more button
            self.driver.find_element_by_xpath(
                '//button[@class="pv-profile-section__card-action-bar pv-skills-section__additional-skills artdeco-container-card-action-bar artdeco-button artdeco-button--tertiary artdeco-button--3 artdeco-button--fluid"]').click()
            #wait 2 seconds
            time.sleep(2)
            #get all knowledges
            knowledges = self.driver.find_elements_by_xpath(
                '//div[@id="skill-categories-expanded"]/div/ol/li/div/div/p')  
            knowledges_and_tools = []
            #browse all knolledges
            for knowledge in knowledges:
                knowledges_and_tools.append(knowledge.text)
        except:
            print("Sorry we found no knowledges or tools for this person!!!")      
        return knowledges_and_tools
    
    def get_contacts(self):
        """function to get contact datas, return a list of dictionnary that contain contact datas"""
        contact=[]
        #click on contact link
        contact_link = self.driver.find_element_by_xpath(
            '//a[@data-control-name="contact_see_more"]').click()
        #wait until presence on the contact section
        contact_section = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
            (By.ID, "pv-contact-info")))
        time.sleep(5)
        #get website container
        website_container = self.driver.find_element_by_class_name(
            'ci-websites')
        #initialise website_info by calling functin extract_website_datas from functions
        website_info = extract_website_datas(website_container)
        contact.append(website_info)
        #get phone container
        phone_container = self.driver.find_element_by_class_name(
            'ci-phone')
        #initialise phone_info by calling functin extract_phone_number from functions
        phone_info = extract_phone_number(phone_container)
        contact.append(phone_info)
        #get address container
        address_container = self.driver.find_element_by_class_name(
            'ci-address')
        #initialise address_info by calling functin extract_address_datas from functions
        address_info = extract_address_datas(address_container)
        contact.append(address_info)
        #get email container
        email_container = self.driver.find_element_by_class_name(
            'ci-email')
        #initialise email_info by calling functin extract_email_datas from functions
        email_info = extract_email_datas(email_container)
        contact.append(email_info)
        return contact