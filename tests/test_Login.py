from tests.BaseTest import TestBaseTest
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from pages.SignInPage import SignInPage
from config.config import TestData

class Test_Login(TestBaseTest):
    def test_login(self):
        accountName = "Test"
        self.homePage.click_login()
        self.signInPage.clickSignInWithImdb()
        self.loginPage.login(TestData.USERNAME, TestData.PASSWORD)
        loginUser = self.homePage.getUserName()
        assert loginUser == accountName

    def test_successful_logout(self):
        self.homePage.click_login()
        self.signInPage.clickSignInWithImdb()
        self.loginPage.login(TestData.USERNAME, TestData.PASSWORD)
        self.homePage.clickLogOutButton()
        loginUser = self.homePage.getUserFieldText()
        assert loginUser == "Sign In"
