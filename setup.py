from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path
import re

here = path.abspath(path.dirname(__file__))

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('linkedin_scraper/__init__.py').read(),
    re.M
    ).group(1)

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
        name = 'scrape_linkedin',
        packages = ['linkedin_scraper'], # this must be the same as the name above
        version = version,
        description = 'A way to scrape user datas from linkedin',
        author = 'Beny Dziengue',
        author_email = 'bdziengue@gmail.com',
        url = 'https://github.com/BenyDZ/Linkedin-Scrapper.git', # use the URL to the github repo
        download_url = 'https://github.com/BenyDZ/Linkedin-Scrapper.git/dist/' + version + '.tar.gz',
        keywords = ['linkedin', 'scraping', 'scraper'], 
        classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
        ],
        install_requires=['webdriver-manager', 'selenium'],
        )