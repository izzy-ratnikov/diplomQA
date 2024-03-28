from selenium.webdriver import Keys

from helpers.base_page import BasePage

from pages.locators.main_locators import MainLocators


class MainPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)
        self.main_locators = MainLocators()

    def find_url_anime(self):
        base_page = BasePage(self.driver)
        return base_page.get_attribute(self.main_locators.BUTTON_ANIME, 'href')

    def find_button_anime(self):
        base_page = BasePage(self.driver)
        return base_page.get_text(self.main_locators.BUTTON_ANIME)

    def click_on_button_characters(self):
        base_page = BasePage(self.driver)
        return base_page.click_on_with_text(self.main_locators.CHARACTERS)

    def click_button_random_anime(self):
        base_page = BasePage(self.driver)
        return base_page.click_on_with_text(self.main_locators.RANDOM_ANIME)

    def write_on_search_string(self, text):
        base_page = BasePage(self.driver)
        base_page.click_on(self.main_locators.BUTTON_SEARCH_STRING)
        base_page.send_keys(self.main_locators.SEARCH_STRING, text)
        return base_page.send_keys(self.main_locators.SEARCH_STRING, Keys.RETURN)

    def choose_anime_with_filters(self):
        base_page = BasePage(self.driver)
        base_page.click_on(self.main_locators.GENRES)
        base_page.click_on(self.main_locators.CHOOSE_GENRES)
        base_page.click_on(self.main_locators.TYPE)
        base_page.click_on(self.main_locators.CHOOSE_TYPE)
        base_page.click_on(self.main_locators.TYPE_OF_VOICE_ACTING)
        base_page.click_on(self.main_locators.CHOOSE_VOICE_ACTING)
        return base_page.click_on(self.main_locators.SEARCH_BUTTON)

    def search_anime_by_date(self):
        base_page = BasePage(self.driver)
        base_page.click_on(self.main_locators.LINE_DATE)
        return base_page.click_on(self.main_locators.SEARCH_BUTTON)

    def check_attribute(self):
        base_page = BasePage(self.driver)
        return base_page.get_attribute(self.main_locators.ATTRIBUTE, "type")

    def send_clear(self):
        base_page = BasePage(self.driver)
        base_page.click_on(self.main_locators.BUTTON_SEARCH_STRING)
        base_page.send_keys(self.main_locators.SEARCH_STRING, "Магическая битва 2")
        base_page.clear_input(self.main_locators.SEARCH_STRING)
        base_page.send_keys(self.main_locators.SEARCH_STRING, "91 день")
        return base_page.send_keys(self.main_locators.SEARCH_STRING, Keys.RETURN)

    def check_clicks(self):
        base_page = BasePage(self.driver)
        base_page.click_release(self.main_locators.BUTTON_ANIME)
        return base_page.double_click(self.main_locators.BUTTON_MANGA)

    def check_keyboard_click(self):
        base_page = BasePage(self.driver)
        base_page.keyboard_click(self.main_locators.BUTTON_ANIME)
        windows = self.driver.window_handles
        return self.driver.switch_to.window(windows[1])

    def check_js_click(self):
        base_page = BasePage(self.driver)
        return base_page.click_by_js(self.main_locators.CHARACTERS_XPATH)

    def check_cookie(self):
        cookie = {"name": "test", "value": "bar"}
        self.driver.add_cookie(cookie)
        cookies = self.driver.get_cookie("test")
        return cookies["name"] == cookie["name"]

    def wait_click(self):
        base_page = BasePage(self.driver)
        return base_page.wait_and_click(self.main_locators.BUTTON_ANIME)

    def footer_elements(self, locator):
        base_page = BasePage(self.driver)
        base_page.scroll_to()
        return base_page.click_on(locator)

    def click_windows(self):
        base_page = BasePage(self.driver)
        main_window = self.driver.current_window_handle  # noqa F841
        base_page.keyboard_click(self.main_locators.BUTTON_ANIME)
        page_two = self.driver.current_window_handle  # noqa F841
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[0])
        self.driver.close()
        return self.driver.switch_to.window(windows[1])

    def site_go_up(self):
        base_page = BasePage(self.driver)
        base_page.scroll_to()
        return base_page.click_on(self.main_locators.SCROLL_UP)

    def footer_elem(self):
        base_page = BasePage(self.driver)
        base_page.scroll_to()
        return base_page.click_on(MainLocators.FOOTER_THIRD)

    def schedule(self):
        base_page = BasePage(self.driver)
        base_page.move_to_element(MainLocators.SCHEDULE_ANIME)
        return base_page.move_to_element(MainLocators.CHOOSE_ANIME_IN_SCHEDULE)
