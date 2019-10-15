==================
Linkedin_Scrapper
==================

A way to scrappe data in linkedin

Installation
============

``
pip install scrape-linkedin
``

Actual product
==============

Person scraper


Coming soon ...
===============

Person scraper : Scraping a person by adding her account link
Company scraper

How to use it?
==============

It's very simple, what you need are just, you're `linkedin email account` and your `password`.
Like a lot of person can have the same name, you need to know the company where he work, it'll easier 
to find the right person like that.

Usage example
-------------

``
#import needed object
from linkedin_scraper import Person, Account

myAccount = Account("youremail@gmail.com", "yourpassword")
#login in linkedin account, return the driver
driver = myAccount.login()

#search a person
person = Person("pankit chheda", "invideo", driver)
person.search()

#get experiences of the person
experiences = person.get_experiences()
``

Experiences
-----------
That is the experiences they have. ``get_experiences()``, it return a list of job titles and companies like **ceo, google**.

Skills
------
That is the skills that they have. ``get_skills()``, return a list of skills.

Training
--------
That is the past educations they have. ``get_training()``, return a list of school names, degrees and domains like **Marien-Ngouaby University, Master, Software Engineering**.

Knowledge and tools
-------------------
That is the knowledge of sector and tools they know. ``get_Knowledges_tools()``, return a list of knowledges and/or tools.

Others
======
Don't need to have any driver. Chrome driver will be automaticaly installed.
Must login just the first time, after that your session will be saved on the driver cookies

Version
=======
Version 1.0.x
* First Publish, only Person scraper