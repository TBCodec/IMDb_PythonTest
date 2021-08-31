from tests.BaseTest import TestBaseTest
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from pages.SignInPage import SignInPage
from config.config import TestData

class Test_Login(TestBaseTest):
    def test_login(self):
        accountName = "Test"
        self.homePage = HomePage(self.driver)
        self.homePage.click_login()
        self.signInPage = SignInPage(self.driver)
        self.signInPage.clickSignInWithImdb()
        self.loginPage = LoginPage(self.driver)
        self.loginPage.login(TestData.USERNAME, TestData.PASSWORD)
        loginUser = self.homePage.getUserName()
        assert loginUser == accountName
