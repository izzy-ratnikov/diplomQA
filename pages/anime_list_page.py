from data.urls import ANIME_LIST_URL
from helpers.base_page import BasePage

from pages.locators.anime_list_locators import AnimeListLocators


class AnimeList(BasePage):

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(ANIME_LIST_URL)
        super().__init__(driver)
        self.anime_list_locators = AnimeListLocators()

    def choose_anime_from_list(self):
        base_page = BasePage(self.driver)
        return base_page.click_on(self.anime_list_locators.CHOOSE_ANIME)
