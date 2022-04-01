#from selenium import webdriver  # import selenium to the file
#from time import sleep
from selenium.webdriver.chrome.service import service
from selenium.webdriver.chrome.webdriver import WebDriver

s = Service(executable_path='../chromedriver.exe')
driver: WebDriver = webdriver.Chrome(service=s)

# Advantage shopping Test Automation Plan
# Launch Advantage Shopping App Website- validate we are on the home page
# Navigate to login page- validate we are on the login page
# login with adin account- validate we are on the dashboard page
# navigate to add New User page -create_account_details> Personal_Create_account> Acct_details > Account> Register - validate we are on the Add new User page
# # submit a new user > Users > Add New User - validate we are on the Add new User page
# populate the new user form fields using faker library fake random data
# summit a new user form
# validate new user added:
# search for a new user new email- validate new is found
# logout of admin account
# login as a new user - validate a new user can log in
# search for a new user using email address
# delete new user

def setup():
        print(f'launch advantage shopping app')
        print(f'..............................................')

        # make browser full screen
        driver.maximize_window()

        # give browser 30 seconds to respond
        driver.implicitly_wait(30)

        # navigate to advantage shopping app website  'https://advantageonlineshopping.com/#/'
        if driver.current_url == 'https://advantageonlineshopping.com/#/':
       #if driver.title == 'advantage shopping':
            print('hurray! advantage shopping app website launched successfully!')
        print(f'advantage shopping homepage URL:{driver.current_url}, Homepage title:{driver.title}')
        sleep(0.30)

        "driver.close()"


        print(f'advantage shopping did not launch. Check your code or application!')
        print(f'current URL:{driver.current_URL},Page title: {driver.title}')
        "driver.close()"


        print(f'advantage shopping did not launch. Check your code or application!')
        print(f'current URL:{driver.current_URL},Page title: {driver.title}')

def tearDown():
    if driver is not None:
        print(f'.....................................')
        print(f'The test is completed at: {datetime.datetime.now()}')

driver.close()

driver.quit()
