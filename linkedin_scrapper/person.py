#import needed object
import time
# from selenium.webdriver.common.keys import Keys
# from selenium import webdrive
# from selenium.webdriver.common.action_chains import ActionChains


class Person():
    def __init__(self, driver):
        """ Constructor for this class """
        #initialise needed object
        self.driver = driver

    def search_by_name_and_key_word(self, full_name, keyword=""):
        """Function to search a person in linkedin by her name and the a key word like company name, 
        take driver, the full name and the domain name on the company where he work"""
        #initialise the object full_name, by getting the full name of the person to search
        self.full_name = full_name
        #initialise the keyword
        self.keyword = keyword
        #get the search bar
        self.search_bar = self.driver.find_element_by_class_name('search-global-typeahead__input')
        #clear search bar
        self.search_bar.clear()
        #fill search bar
        self.search_bar.send_keys(self.full_name + " " + self.keyword)
        #wait 1 seconde
        time.sleep(2)
        #click on Enter button
        self.search_bar.send_keys(u'\ue007')
        if self.keyword != "":
            #wait 2 secondes
            time.sleep(5)
            #get and click on person links
            self.driver.find_elements_by_tag_name('h3')[-1].click()
        else:
            
    
    def search_by_account_link(self, account_link):
        """Function to search a person by her """
        #open accoubt link in the driver
        self.account_link = account_link
        self.driver.get(self.account_link)

    def get_experiences(self):
        """ function to get experiences datas """
        #wait 3 secondes
        time.sleep(5)
        #click on button see more
        try:
            self.see_more_button = self.driver.find_element_by_xpath('//button[@class="pv-profile-section__see-more-inline pv-profile-section__text-truncate-toggle link link-without-hover-state"]').click()
        except:
            pass
        #wait 1 secondes
        time.sleep(5)
        #get all job_titles datas
        self.job_titles = self.driver.find_elements_by_xpath('//h3[@class="t-16 t-black t-bold"]')
        #get all company_names
        self.company_names = self.driver.find_elements_by_xpath('//p[@class="pv-entity__secondary-title t-14 t-black t-normal"]')
        self.experiences = []
        #browse all company name and job titles in same times
        for self.job_title, self.company_name in zip(self.job_titles, self.company_names):
            #add job titles and companies names in the list experiences
            self.experiences.append(self.job_title.text + ", " + self.company_name.text)       
        return self.experiences
    
    def get_training(self):
        """Function to get all formation datas"""
        #wait 5 secondes
        time.sleep(5)
        #get all school formation name
        self.school_names = self.driver.find_elements_by_xpath('//h3[@class="pv-entity__school-name t-16 t-black t-bold"]')
        #get all degrees title
        self.degrees = self.driver.find_elements_by_xpath('//p[@class="pv-entity__secondary-title pv-entity__degree-name t-14 t-black t-normal"]/span')
        #get all formation domain
        self.domains = self.driver.find_elements_by_xpath('//p[@class="pv-entity__secondary-title pv-entity__fos t-14 t-black t-normal"]/span')
        self.trainig = []
        #browse all school_names, degrees, domain in the same time
        for self.school_name, self.degree, self.domain in zip(self.school_names, self.degrees, self.domains):
            self.trainig.append(self.school_name.text + ", " + self.degree.text + ", " + self.domain.text)
        return self.trainig
    
    def get_skills(self):
        """Function to get all skills datas"""
        #wait 5 secondes
        time.sleep(5)
        #get all school formation name
        self.school_names = self.driver.find_elements_by_xpath('//h3[@class="pv-entity__school-name t-16 t-black t-bold"]')
        #scroll until the last school names come into viewport
        self.school_names[-1].location_once_scrolled_into_view
        #wait 2 secondes
        time.sleep(2)
        #get all skills
        self.skills_names = self.driver.find_elements_by_xpath('//ol[@class="pv-skill-categories-section__top-skills pv-profile-section__section-info section-info pb1"]/li/div/div/p')    
        self.skills = []
        #browse all skills
        for self.skill in self.skills_names:
            self.skills.append(self.skill.text)     
        return self.skills

    def get_knowledges_tools(self):
        """ Function to get all Knowledges datas """
        #wait 5 secondes
        time.sleep(5)
        #get all school formation name
        self.school_names = self.driver.find_elements_by_xpath('//h3[@class="pv-entity__school-name t-16 t-black t-bold"]')
        #scroll until the last school names come into viewport
        self.school_names[-1].location_once_scrolled_into_view
        #wait 2 secondes
        time.sleep(2)
        try:
            #click on the see more button
            self.driver.find_element_by_xpath('//button[@class="pv-profile-section__card-action-bar pv-skills-section__additional-skills artdeco-container-card-action-bar artdeco-button artdeco-button--tertiary artdeco-button--3 artdeco-button--fluid"]').click()
            #wait 2 seconds
            time.sleep(2)
            #get all knowledges
            self.knowledges = self.driver.find_elements_by_xpath('//div[@id="skill-categories-expanded"]/div/ol/li/div/div/p')
            
            self.knowledges_and_tools = []
            #browse all knolledges
            for self.knowledge in self.knowledges:
                self.knowledges_and_tools.append(self.knowledge.text)
        except:
            print("Sorry we found no knowledges or tools for this person!!!")      
        return self.knowledges_and_tools
    
    def get_contacts(self):
        pass