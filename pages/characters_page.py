from data.urls import CHARACTERS_URL
from helpers.base_page import BasePage

from pages.locators.characters_locators import CharactersLocators


class Characters(BasePage):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)
        self.driver.get(CHARACTERS_URL)
        self.characters_locators = CharactersLocators()

    def choose_character_in_list(self):
        base_page = BasePage(self.driver)
        return base_page.click_on(self.characters_locators.SELECT_CHARACTER)
