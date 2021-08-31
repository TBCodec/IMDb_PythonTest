from config.config import TestData
from tests.BaseTest import TestBaseTest


class Test_ChangeDataTest(TestBaseTest):
    def test_ChangeDataInProfileBio(self):
        textToBio = "Test Bio field"
        self.homePage.click_login()
        self.signInPage.clickSignInWithImdb()
        self.loginPage.login(TestData.USERNAME, TestData.PASSWORD)
        self.homePage.clickUserNameButton()
        self.homePage.clickAccountSetting()
        self.accountSettingPage.clickEditProfile()
        self.editProfilePage.clearBioField()
        self.editProfilePage.writeToBioField(textToBio)
        self.editProfilePage.clickSaveDescription()
        self.accountSettingPage.clickEditProfile()
        assert textToBio == self.editProfilePage.getTextFromBio()
