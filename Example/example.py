#import needed object
import linkedin_scraper


myAccount = Account.login("patdenzoungany@gmail.com", "Bermanpat18")
#login in linkedin account, return the driver with the current url
driver = myAccount.login()

person = Person("pankit chheda", "invideo", driver)
person.search()
person.get_Knowledges_tools()