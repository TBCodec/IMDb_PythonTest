from selenium import webdriver
from config.config import TestData
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from pages.SignInPage import SignInPage
from pages.AccountSettingPage import AccountSettingPage
from pages.EditProfilePage import EditProfilePage

class TestBaseTest(object):
    def setup(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")
        self.driver.get(TestData.BASE_URL)
        self.homePage = HomePage(self.driver)
        self.signInPage = SignInPage(self.driver)
        self.loginPage = LoginPage(self.driver)
        self.accountSettingPage = AccountSettingPage(self.driver)
        self.editProfilePage = EditProfilePage(self.driver)

    def teardown(self):
        self.driver.close()

