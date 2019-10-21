def extract_website_datas(website_container):
    """Function to extract website datas, return a dictionary with the name of the header like
    key and a list of link of websites like value"""
    website_info={}
    #get all website links 
    links_containers = website_container.find_elements_by_tag_name('a')
    #initialise object website_links, that will contain a list of website links
    website_links=[]
    #browse all object in links_containers
    for elements in links_containers:
        #get and add website link in websites_links
        website_links.append(elements.get_attribute('href'))
    #add header like key and website_links like value in website_info
    website_info["Websites"] = website_links
    return website_info

def extract_phone_number(phone_container):
    """Function to extract phone numbers, return a dictionary with the name of the header like
    key and a list of phone numbers like value"""
    phone_info={}
    #get all website links 
    phone_number = phone_container.find_element_by_xpath(
        '//span[@class="t-14 t-black t-normal"]').text
    phone_info["Phone number"] = phone_number
    return phone_info

def extract_address_datas(address_container):
    """Function to extract address infos, return a dictionary with the name of the header like
    key and the address name plus the google map link of the address like value"""
    address_info={}
    #get all website links 
    adress_container = address_container.find_element_by_tag_name('a')
    address = adress_container.text
    address_google_maps_link = adress_container.get_attribute('href')
    address_info["Address"] = address
    address_info["Map link"] = address_google_maps_link
    return address_info

def extract_email_datas(email_container):
    """Function to extract email infos, return a dictionary with the name of the header like
    key and the mail like value"""
    email_info={}
    #get email
    email = email_container.find_element_by_tag_name('a').get_attribute('href')
    email = email.split(":")[1]
    email_info["Email"] = email
    return email_info