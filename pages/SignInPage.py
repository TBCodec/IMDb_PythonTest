from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from pages.BasePage import BasePage

class SignInPage(BasePage):
    SIGIN_LIST = (By.XPATH, "//div[@id='signin-options']//a[@href]")

    def __init__(self, driver):
        super().__init__(driver)

    def clickChoosedButton(self, buttonName):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(self.SIGIN_LIST))
        signInChoose = self.driver.find_elements_by_xpath("//div[@id='signin-options']//a[@href]")
        for element in signInChoose:
            if buttonName in element.text:
                element.click()
                break

    def clickSignInWithImdb(self):
        self.clickChoosedButton("IMDb")
