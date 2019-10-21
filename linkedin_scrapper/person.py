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
            time.sleep(2)
            #get and click on person links
            self.driver.find_elements_by_tag_name('h3')[-1].click()
            time.sleep(2)
        else:
            #wait 2 secondes
            time.sleep(2)
            search_result = self.driver.find_elements_by_tag_name('h3')
            #check if search result is upper than 2
            if len(search_result) > 2:
                #click on the first result
                search_result[1].click()
            #wait 2 secondes
            time.sleep(2)
            
            
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
        #get all employements dates
        employements_dates = self.driver.find_elements_by_class_name(
            'pv-entity__date-range')
        #get all duration of employements
        duration_of_employements = self.driver.find_elements_by_class_name(
            'pv-entity__bullet-item-v2')
        #get all locations
        locations = self.driver.find_elements_by_class_name(
            'pv-entity__location')
        list_of_experiences=[]
        index=1
        #browse all company name and job titles in same times
        for job_title, company_name, employement_date, duration_of_employement, location in zip(
            job_titles, company_names, employements_dates, duration_of_employements, locations):
            globals()["experiences" + str(index)]={}
            globals()["experiences" + str(index)]["Job title"] = job_title.text
            globals()["experiences" + str(index)]["Company"] = company_name.text
            globals()["experiences" + str(index)]["Employement date"] = employement_date.text.split("\n")[1]
            globals()["experiences" + str(index)]["Duration of employement"] = duration_of_employement.text
            globals()["experiences" + str(index)]["Location"] = location.text.split("\n")[1]
            list_of_experiences.append(globals()["experiences" + str(index)])
            index += 1
        return list_of_experiences
    
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
        durations = self.driver.find_elements_by_class_name('pv-entity__dates')
        activities = self.driver.find_elements_by_class_name('activities-societies')
        descriptions = self.driver.find_elements_by_class_name('pv-entity__description')
        list_of_trainig = []
        index=1
        #browse all school_names, degrees, domain in the same time
        for school_name, degree, domain, duration, activity, description  in zip(
            school_names, degrees, domains, durations, activities, descriptions):
            globals()["training" + str(index)]={}
            globals()["training" + str(index)]["School name"] = school_name.text
            globals()["training" + str(index)]["Degree"] = degree.text
            globals()["training" + str(index)]["Domain"] = domain.text
            globals()["training" + str(index)]["Duration"] = duration.text.split("\n")[1]
            globals()["training" + str(index)]["Activity"] = activity.text
            globals()["training" + str(index)]["Description"] = description.text
            list_of_trainig.append(globals()["training" + str(index)])
            index += 1
        return list_of_trainig
   
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
        knowledges_and_tools = []
        try:
            #click on the see more button
            self.driver.find_element_by_xpath(
                '//button[@class="pv-profile-section__card-action-bar pv-skills-section__additional-skills artdeco-container-card-action-bar artdeco-button artdeco-button--tertiary artdeco-button--3 artdeco-button--fluid"]').click()
            #wait 2 seconds
            time.sleep(2)
            #get all knowledges
            knowledges = self.driver.find_elements_by_xpath(
                '//div[@id="skill-categories-expanded"]/div/ol/li/div/div/p')  
            #browse all knolledges
            for knowledge in knowledges:
                knowledges_and_tools.append(knowledge.text)
        except:
            print("Sorry we found no knowledges or tools for this person!!!")      
        return knowledges_and_tools
    
    def get_contacts(self):
        """function to get contact datas, return a list of dictionnary that contain contact datas"""
        contact={}
        #click on contact link
        contact_link = self.driver.find_element_by_xpath(
            '//a[@data-control-name="contact_see_more"]').click()
        #wait until presence on the contact section
        contact_section = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
            (By.ID, "pv-contact-info")))
        time.sleep(1)
        try:
            #get website container
            website_container = self.driver.find_element_by_class_name(
                'ci-websites')
            #initialise website_info by calling functin extract_website_datas from functions
            website_info = extract_website_datas(website_container)
            contact["Websites"] = website_info["Websites"]
        except:
            print('There is no website available for this user')
        try:
            #get phone container
            phone_container = self.driver.find_element_by_class_name(
                'ci-phone')
            #initialise phone_info by calling functin extract_phone_number from functions
            phone_info = extract_phone_number(phone_container)
            contact["Phone number"] = phone_info["Phone number"]
        except:
            print('There is no phone number available for this user')
        try:
            #get address container
            address_container = self.driver.find_element_by_class_name(
                'ci-address')
            #initialise address_info by calling functin extract_address_datas from functions
            address_info = extract_address_datas(address_container)
            contact["Address"] = address_info["Address"]
            contact["Map link"] = address_info["Map link"]
        except:
            print('There is no address available for this user')
        try:
            #get email container
            email_container = self.driver.find_element_by_class_name(
                'ci-email')
            #initialise email_info by calling functin extract_email_datas from functions
            email_info = extract_email_datas(email_container)
            contact["Email"] = email_info["Email"]
        except:
            print('There is no email address available for this user')
        return contact