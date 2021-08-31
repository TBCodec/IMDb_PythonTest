from selenium.webdriver.common.by import By

from pages.BasePage import BasePage

class AccountSettingPage(BasePage):

    EDIT_PROFILE_BUTTON = (By.XPATH, "//a[contains(@href,\"edit\")]")

    def __init__(self, driver):
        super().__init__(driver)

    def clickEditProfile(self):
        self.do_click(self.EDIT_PROFILE_BUTTON)