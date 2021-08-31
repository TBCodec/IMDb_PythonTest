from selenium import webdriver
from config.config import TestData

class TestBaseTest(object):
    def setup(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")
        self.driver.get(TestData.BASE_URL)

    def teardown(self):
        self.driver.close()

