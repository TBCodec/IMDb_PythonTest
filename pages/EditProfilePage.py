from selenium.webdriver.common.by import By

from pages.BasePage import BasePage

class EditProfilePage(BasePage):
    BIO_FIELD = (By.XPATH, "//textarea")
    SAVE_DESCRIPTION_BUTTON = (By.XPATH, "//div[contains(@data-save-redirect,\"account\")]")

    def __init__(self, driver):
        super().__init__(driver)

    def writeToBioField(self, text):
        self.do_send_keys(self.BIO_FIELD, text)

    def clickSaveDescription(self):
        self.do_click(self.SAVE_DESCRIPTION_BUTTON)

    def clearBioField(self):
        self.clear_element_text(self.BIO_FIELD)

    def getTextFromBio(self):
        return self.get_element_text(self.BIO_FIELD)