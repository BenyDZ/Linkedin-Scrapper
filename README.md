# Linkedin_Scrapper
A way to scrappe data in linkedin

# Installation
```
pip install linkedin-scrapper
```

# Product
Person scraper

Company scraper (Coming soon)

# How to use it?
It's very simple, what you need are just, you're `linkedin email account` and your `password`.
After, you have two choice to make a search, with an account link or with a full name and a keyword if possible.
Like a lot of person can have the same name, a specific keyword to find them can be important.

### Usage example
```
#import needed object
from linkedin_scrapper import Person, Account


myAccount = Account("your_email@gmail.com", "your_password", "your_driver")
#login in linkedin account, return the driver with the current url
driver = myAccount.login()

person = Person(driver)
person.search_by_account_link('https://www.linkedin.com/in/beny-dziengue-a3591a188')
knowledges = person.get_knowledges_tools()
print(knowledges)
```

# Person-Scrapper

Availlable function for scraping users datas

## Search :
### Search by account link
This function alloow you to search a person by using her account link. `search_by_account_link()`. It taking like paramater the account link of the person you wanted to scrape.

### Search by name and key word
This function allow you to search a person by using her name and a key word (like the name of the company where her work, school, ...) To be as precise as possible. 
`search_by_name_and_key_word()`, take the full name of the person and a key word. Note that the key word is optionally.But we recommend you to use a keyword to refine the search, we only take into account the first result of the search.

### Experiences
That is the experiences they have. `get_experiences()`, it return a list of job titles and companies like `ceo, google`.

### skills
That is the skills that they have. `get_skills()`, return a list of skills.

### Training
That is the past educations they have. `get_training()`, return a list of school names, degrees and domains like `Marien-Ngouaby University, Master, Software Engineering`.

### Knowledge and tools
That is the knowledge of sector and tools they know. `get_knowledges_tools()`, return a list of knowledges and/or tools.

## Drivers
Don't need to have any driver exe files. Just enter a driver name and it will be installed.
Names of availlable drivers are :
* chrome : For chromedriver
* firefox : For geckodriver
* ie : For internet explorer driver
* edge : For microsoft edge driver

# Version

Version 1.0

* First Publish, only Person scraper