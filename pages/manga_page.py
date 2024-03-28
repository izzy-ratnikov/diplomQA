from data.urls import MANGA_URL
from helpers.base_page import BasePage

from pages.locators.manga_locators import MangaLocators


class Manga(BasePage):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)
        self.driver.get(MANGA_URL)
        self.manga_locators = MangaLocators()

    def choose_manga_in_list(self):
        base_page = BasePage(self.driver)
        return base_page.click_on(self.manga_locators.SELECT_MANGA)

    def sorted_manga(self):
        base_page = BasePage(self.driver)
        base_page.click_on(self.manga_locators.SORT_BUTTON)
        base_page.click_on(self.manga_locators.CHOOSE_SORT)
        return base_page.wait_another_url(MANGA_URL)
