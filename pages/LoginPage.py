from selenium.webdriver.common.by import By

from pages.BasePage import BasePage

class LoginPage(BasePage):

    USER_NAME_FIELD = (By.XPATH, "//*[@id=\"ap_email\"]");
    PASSWORD_FIELD = (By.XPATH, "//*[@id=\"ap_password\"]");
    SIGNIN_BUTTON = (By.ID, "signInSubmit");
    AUTH_WARNING_MESSAGE_BOX = (By.ID, "auth-warning-message-box");

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, userName, password):
        self.setField(self.USER_NAME_FIELD, userName)
        self.setField(self.PASSWORD_FIELD, password)
        self.do_click(self.SIGNIN_BUTTON)

    def setField(self, by_locator, text):
        self.do_click(by_locator)
        self.do_send_keys(by_locator, text)
