from helpers.base_page import BasePage
from pages.locators.login_locators import LoginLocators


class LoginPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)
        self.driver.get('https://animego.org/login')
        self.login_locators = LoginLocators()

    def login_box(self):
        base_page = BasePage(self.driver)
        base_page.send_keys_css(self.login_locators.LOGIN, "stylebender")
        base_page.send_keys_css(self.login_locators.PASSWORD, '123443')
        return base_page.click_on_css(self.login_locators.BUTTON_LOGIN)
