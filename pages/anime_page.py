from helpers.base_page import BasePage
from pages.locators.anime_locators import AnimeLocators


class AnimePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.anime_locators = AnimeLocators()

    def watch_trailer_anime(self):
        self.driver.get('https://animego.org/anime/magiya-i-muskuly-2-2493')
        base_page = BasePage(self.driver)
        base_page.click_on(self.anime_locators.BUTTON_PLAY_TRAILER)
        return base_page.get_attribute(self.anime_locators.BUTTON_PLAY_TRAILER, 'href')

    def related_anime(self):
        self.driver.get('https://animego.org/anime/agent-vremeni-2-2343')
        base_page = BasePage(self.driver)
        return base_page.click_on(self.anime_locators.CHOOSE_RELATED)

    def find_name_anime(self):
        self.driver.get("https://animego.org/anime/magicheskaya-bitva-2-2332")
        base_page = BasePage(self.driver)
        return base_page.get_text(self.anime_locators.TEXT_ANIME_NAME)

    def eighteen_years_no(self):
        self.driver.get("https://animego.org/anime/podnyatie-urovnya-v-odinochku-2477")
        base_page = BasePage(self.driver)
        self.driver.execute_script("window.scrollTo(0, 1500);")
        base_page.wait_and_click(self.anime_locators.BUTTON_NO)
        return base_page.get_text(self.anime_locators.TEXT_YEARS)

    def eighteen_years_yes(self):
        self.driver.get("https://animego.org/anime/podnyatie-urovnya-v-odinochku-2477")
        base_page = BasePage(self.driver)
        self.driver.execute_script("window.scrollTo(0, 1500);")
        return base_page.wait_and_click(self.anime_locators.BUTTON_YES)

    def reviews(self):
        self.driver.get("https://animego.org/anime/agent-vremeni-2-2343")
        base_page = BasePage(self.driver)
        return base_page.click_on(AnimeLocators.READ_ALL_REVIEWS)

    def status(self):
        self.driver.get("https://animego.org/anime/agent-vremeni-2-2343")
        base_page = BasePage(self.driver)
        return base_page.click_on(AnimeLocators.STATUS_BUTTON)
