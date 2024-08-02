from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def login_url(self, url):
        self.driver.get(url)

    def username(self, username):
        email = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginLocator.EMAIL_FIELD)

                                                        )
        username = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginLocator.ENTER_))
        enter_username.send_keys(username)

    def password(self, password):
        enter_password = WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located(LoginLocator.ENTER_PASSWORD))
        enter_password.send_keys(password)

    def click_login(self):
        click_login = WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located(LoginLocator.CLICK_LOGIN_BUTTON))
        click_login.click()






