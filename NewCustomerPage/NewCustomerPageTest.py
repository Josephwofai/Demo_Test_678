from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from NewCustomerLocator.NewCustomerLocatorTest import NewCustomerLocator

class NewCustomerPage:

    def __init__(self, driver):
        self.driver = driver

    def new_customer(self):
        new_customer = WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located(NewCustomerLocator.CLICK_NEW_CUSTOMER))
        new_customer.click()

    def email(self):
        enter_email = WebDriverWait(self.drver, timeout=10).until(
            EC.presence_of_element_located(NewCustomerLocator.ENTER_EMAIL))
        enter_email.send_keys(email)

    def firstname(self):
        enter_firstname = WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located(NewCustomerLocator.ENTER_FIRSTNAME))
        enter_firstname.send_keys(firstname)

    def lastname(self):
        enter_lastname = WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located(NewCustomerLocator.ENTER_LASTNAME))
        enter_lastname.send_keys(lastname)

    def city(self):
        enter_city = WebDriverWait(str.driver, timeout=10).until(
            EC.presence_of_element_located(NewCustomerLocator.ENTER_CITY))
        enter_city.send_keys(city)

    def state(self):
        enter_state = WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located(NewCustomerLocator.ENTER_STATE))
        enter_state.send_keys(state)

    def gender(self):
        enter_gender = WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located(NewCustomerLocator.ENTER_GENDER))
        enter_gender.send_keys(gender)

    def promotional_list(self):
        click_promotional_list = WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located(NewCustomerLocator.CLICK_PROMOTIONAL_LIST))
        click_promotional_list.click()

    def submit(self):
        click_submit = WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located(NewCustomerLocator.CLICK_SUBMIT))
        click_submit.click()



