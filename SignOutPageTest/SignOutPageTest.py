from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from SignOutLocatorTest.SignOutLocatorTest import SignOutLocator


class SignOutPage:

    def __init__(self, driver):
        self.driver = driver

    def sign_out(self):
        click_sign_out = WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located(NewCustomerLocator.CLICK_SIGN_OUT))
        click_sign_out.click()
