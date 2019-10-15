#import needed object
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

class Person():
    def __init__(self, fullName, companyName, driver):
        """ Constructor for this class """
        
        #initialise needed object
        self.fullName = fullName
        self.companyName = companyName
        self.driver = driver

    def search(self):
        """
        Function to search a person in linkedin, take driver, the full name and the domain name on the company
        where he work
        """

        #get the search bar
        self.searchBar = self.driver.find_element_by_class_name('search-global-typeahead__input')
        #clear search bar
        self.searchBar.clear()
        #fill search bar
        self.searchBar.send_keys(self.fullName + " " + self.companyName)

        #wait 1 seconde
        time.sleep(1)
        #click on Enter
        self.searchBar.send_keys(u'\ue007')
        #wait 2 secondes
        time.sleep(5)
        #get and click on person links
        self.driver.find_elements_by_tag_name('h3')[-1].click()
    
    def get_experiences(self):
        """ function to get experiences datas """

        #wait 3 secondes
        time.sleep(5)
        #click on button see more
        try :
            self.seeMoreButton = self.driver.find_element_by_xpath('//button[@class="pv-profile-section__see-more-inline pv-profile-section__text-truncate-toggle link link-without-hover-state"]').click()
        except :
            pass
        #wait 1 secondes
        time.sleep(1)
        #get all jobTitles datas
        self.jobTitles = self.driver.find_elements_by_xpath('//h3[@class="t-16 t-black t-bold"]')
        #get all companyNames
        self.companyNames = self.driver.find_elements_by_xpath('//p[@class="pv-entity__secondary-title t-14 t-black t-normal"]')

        self.experiences = []
        #browse all company name and job titles in same times
        for self.jobTitle, self.companyName in zip(self.jobTitles,self.companyNames):
            #add job titles and companies names in the list experiences
            self.experiences.append(self.jobTitle.text + ", " + self.companyName)
        
        return self.experiences
    
    def get_training(self):
        """Function to get all formation datas"""

        #wait 5 secondes
        time.sleep(5)
        #get all school formation name
        self.schoolNames = self.driver.find_elements_by_xpath('//h3[@class="pv-entity__school-name t-16 t-black t-bold"]')
        #get all degrees title
        self.degrees = self.driver.find_elements_by_xpath('//p[@class="pv-entity__secondary-title pv-entity__degree-name t-14 t-black t-normal"]/span')
        #get all formation domain
        self.domains = self.driver.find_elements_by_xpath('//p[@class="pv-entity__secondary-title pv-entity__fos t-14 t-black t-normal"]/span')

        self.trainig = []
        #browse all schoolNames, degrees, domain in the same time
        for self.schoolName, self.degree, self.domain in zip(self.schoolNames, self.degrees, self.domains):
            self.trainig.append(self.schoolName.text + ", " + self.degree.text + ", " + self.domain.text)
        
        return self.trainig
    
    def get_skills(self):
        """Function to get all skills datas"""
        
        #wait 5 secondes
        time.sleep(5)
        #get all school formation name
        self.schoolNames = self.driver.find_elements_by_xpath('//h3[@class="pv-entity__school-name t-16 t-black t-bold"]')
        #scroll until the last school names come into viewport
        self.schoolNames[-1].location_once_scrolled_into_view
        #wait 2 secondes
        time.sleep(2)
        #get all skills names
        self.skillsNames = self.driver.find_elements_by_xpath('//ol[@class="pv-skill-categories-section__top-skills pv-profile-section__section-info section-info pb1"]/li/div/div/p')
        
        self.skills = []
        #browse all skills
        for self.skill in self.skillsNames:
            self.skills.append(self.skill.text)
        
        return self.skills

    def get_Knowledges_tools(self):
        """ Function to get all Knowledges datas """

        #wait 5 secondes
        time.sleep(5)
        #get all school formation name
        self.schoolNames = self.driver.find_elements_by_xpath('//h3[@class="pv-entity__school-name t-16 t-black t-bold"]')
        #scroll until the last school names come into viewport
        self.schoolNames[-1].location_once_scrolled_into_view
        #wait 2 secondes
        time.sleep(2)
        try :
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
