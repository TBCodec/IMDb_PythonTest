from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class HomePage(BasePage):

    LOGIN_BUTTON = (By.XPATH, "//*[@id=\"imdbHeader\"]//a[@href=\"/registration/signin?ref=nv_generic_lgin\"]")
    USER_NAME_FIELD = (By.XPATH, "//*[@id=\"imdbHeader\"]//div[@class=\"ipc-button__text\"]/span[contains(@class,\"account\")]")
    PRIVACY_POLICY = (By.XPATH, "//a[contains(@href,'/privacy')]")
    MENU_BUTTON = (By.ID, "imdbHeader-navDrawerOpen--desktop")
    MENU_LIST = (By.XPATH, "//*[@id=\"imdbHeader\"]//a")
    SEARCH_CATEGORY_BUTTON = (By.XPATH, "//*[@id=\"nav-search-form\"]/div[contains(@class,\"SearchCat\")]")
    ADVANCED_SEARCH_BUTTON = (By.XPATH, "//a[@href='https://www.imdb.com/search/']")
    ACCOUNT_SETTINGS_BUTTON = (By.XPATH, "//*[@id=\"navUserMenu-contents\"]//a[contains(@href,\"account\")]")

    def __init__(self, driver):
        super().__init__(driver)

    def click_login(self):
        self.do_click(self.LOGIN_BUTTON)

    def getUserName(self):
        username = self.get_element_text(self.USER_NAME_FIELD)
        return username