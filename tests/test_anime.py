import allure
import pytest

from data.urls import URL_ANIME_WITH_FILTERS
from helpers.base_page import BasePage
from pages.anime_list_page import AnimeList
from pages.anime_page import AnimePage
from pages.characters_page import Characters

from pages.locators.anime_list_locators import AnimeListLocators
from pages.locators.anime_locators import AnimeLocators
from pages.locators.characters_locators import CharactersLocators
from pages.locators.footer_locators import FooterLocators
from pages.locators.main_locators import MainLocators
from pages.locators.manga_locators import MangaLocators
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.manga_page import Manga


@pytest.mark.parametrize("locator", [MainLocators.BUTTON_ANIME,
                                     MainLocators.BUTTON_MANGA])
@pytest.mark.button
@allure.title("Test URL Anime, Manga page")
def test_site_anime_url(driver, locator):
    base_page = BasePage(driver)
    base_page.wait_and_click(locator)
    assert driver.current_url == 'https://animego.org/anime' or 'https://animego.org/manga'


@allure.title("Test attribute AnimePage")
def test_anime_attribute(driver):
    main_page = MainPage(driver)
    assert main_page.find_url_anime() in 'https://animego.org/anime'


@pytest.mark.button
@allure.title("Test title AnimePage")
def test_anime_characters_title(driver):
    main_page = MainPage(driver)
    main_page.click_on_button_characters()
    assert driver.title == 'Список аниме персонажей'


@allure.title("Test scroll")
def test_anime_scroll(driver):
    base_page = BasePage(driver)
    base_page.scroll_to()
    assert base_page.get_text(MainLocators.TEXT_END_PAGE) == "На AnimeGO – только бесплатные аниме без регистрации"


@pytest.mark.parametrize("first_locator", [MainLocators.FOOTER_FIRST,
                                           MainLocators.FOOTER_SECOND])
@allure.title("Test checked footer elements")
def test_footer_elements(driver, first_locator):
    main_page = MainPage(driver)
    base_page = BasePage(driver)
    main_page.footer_elements(first_locator)
    assert base_page.get_text(
        FooterLocators.FOOTER_LOC) == "Пользовательское соглашение" or "Политика конфиденциальности персональных данных"


@allure.title("Test text")
def test_anime_text(driver):
    main_page = MainPage(driver)
    assert main_page.find_button_anime() == "Аниме"


@pytest.mark.parametrize('text', ["91 день", "магическая битва", "тетрадь смерти"])
@allure.title("Test search anime")
def test_anime_search(driver, text):
    main_page = MainPage(driver)
    main_page.write_on_search_string(text)
    assert driver.current_url == "https://animego.org/search/all?q=91+день" or \
           "https://animego.org/search/all?q=магическая+битва" or \
           "https://animego.org/search/all?q=тетрадь+смерти"


@pytest.mark.button
@allure.title("Test random anime")
def test_anime_random(driver):
    main_page = MainPage(driver)
    base_page = BasePage(driver)
    main_page.click_button_random_anime()
    assert base_page.get_locator_css(AnimeLocators.STAR_RATING)


@pytest.mark.xfail(reason="fixing box 'login'")
@allure.title("Test login")
def test_anime_login(driver):
    login_page = LoginPage(driver)
    login_page.login_box()
    assert driver.current_url == 'https://animego.org/profile/'


@allure.title("Test treller")
def test_anime_short_video(driver):
    anime_page = AnimePage(driver)
    assert anime_page.watch_trailer_anime() in "https://www.youtube.com/embed/zk0YBvw53MI"


@allure.title("Test anime filter")
def test_anime_filter(driver):
    main_page = MainPage(driver)
    main_page.choose_anime_with_filters()
    assert driver.current_url == URL_ANIME_WITH_FILTERS


@allure.title("Test filter by date")
def test_anime_filter_by_date(driver):
    main_page = MainPage(driver)
    main_page.search_anime_by_date()
    assert driver.current_url == "https://animego.org/anime/filter/year-from-1991/apply"


@allure.title("Test related")
def test_anime_related(driver):
    anime_page = AnimePage(driver)
    anime_page.related_anime()
    assert driver.current_url == "https://animego.org/anime/agent-vremeni-1780"


@allure.title("Test choose anime")
def test_select_anime_in_list(driver):
    anime_list = AnimeList(driver)
    base_page = BasePage(driver)
    anime_list.choose_anime_from_list()
    assert base_page.get_locator_xpath(AnimeLocators.WATCH_BUTTON)


@allure.title("Test choose character")
def test_choose_anime_character(driver):
    character = Characters(driver)
    base_page = BasePage(driver)
    character.choose_character_in_list()
    assert base_page.get_locator_xpath(CharactersLocators.CHARACTER_DESCRIPTION)


@allure.title("Test select manga")
def test_select_manga(driver):
    manga = Manga(driver)
    base_page = BasePage(driver)
    manga.choose_manga_in_list()
    assert base_page.get_locator_xpath(MangaLocators.MANGA_CHAPTER)


@allure.title("Test sorted manga")
def test_choose_sorted_manga(driver):
    manga = Manga(driver)
    manga.sorted_manga()
    assert driver.current_url == "https://animego.org/manga?sort=r.rating&direction=desc"


@allure.title("Test find text")
def test_find_text(driver):
    anime_page = AnimePage(driver)
    assert "Магическая битва 2" == anime_page.find_name_anime()


@allure.title("Test find attribute")
def test_attribute(driver):
    main_page = MainPage(driver)
    assert main_page.check_attribute() == "image/png"


@allure.title("Test send and clear")
def test_send_clear(driver):
    main_page = MainPage(driver)
    main_page.send_clear()
    assert driver.current_url == "https://animego.org/search/all?q=91+%D0%B4%D0%B5%D0%BD%D1%8C"


@allure.title("Test clicks")
def test_clicks(driver):
    main_page = MainPage(driver)
    main_page.check_clicks()
    assert driver.current_url == "https://animego.org/manga"


@allure.title("Test choose schedule")
def test_choose_anime_schedule(driver):
    main_page = MainPage(driver)
    base_page = BasePage(driver)
    main_page.schedule()
    assert base_page.get_locator_xpath(AnimeLocators.WATCH_BUTTON)


@allure.title("Test keyboard click")
def test_keyboard_click(driver):
    main_page = MainPage(driver)
    base_page = BasePage(driver)
    main_page.check_keyboard_click()
    assert base_page.get_locator_xpath(AnimeListLocators.SORT_BUTTON)


@allure.title("Test js click")
def test_js_click(driver):
    main_page = MainPage(driver)
    main_page.check_js_click()
    assert driver.current_url == "https://animego.org/characters"


@allure.title("Test cookie")
def test_cookie(driver):
    main_page = MainPage(driver)
    assert main_page.check_cookie()


@allure.title("Test wait and click")
def test_wait_and_click(driver):
    main_page = MainPage(driver)
    main_page.wait_click()
    assert driver.current_url == "https://animego.org/anime"


@allure.title("Test windows")
def test_windows(driver):
    main_page = MainPage(driver)
    base_page = BasePage(driver)
    main_page.click_windows()
    assert base_page.get_locator_xpath(AnimeListLocators.FILTER)


@pytest.mark.xfail(reason="AssertionError, with the same text")
@allure.title("Test anime for eighteen years old, press button no")
def test_anime_for_eighteen_years_old_no(driver):
    anime_page = AnimePage(driver)
    assert "Это видео имеет ограничение по возрасту." \
           "Возвращайтесь, когда вам исполнится 18!" == anime_page.eighteen_years_no()


@allure.title("Test anime for eighteen years old, press button yes")
def test_for_eighteen_years_old_yes(driver):
    anime_page = AnimePage(driver)
    base_page = BasePage(driver)
    anime_page.eighteen_years_yes()
    assert base_page.get_locator_xpath(AnimeLocators.VIDEO_PLAYERS)


@pytest.mark.parametrize("locator", [MainLocators.ELEMENT_ONE,
                                     MainLocators.ELEMENT_TWO,
                                     MainLocators.ELEMENT_THREE])
@allure.title("Test scroll up and check elements top of page")
def test_scroll_up_check_top_elements(driver, locator):
    main_page = MainPage(driver)
    base_page = BasePage(driver)
    main_page.site_go_up()
    base_page.move_to_element(locator)
    assert driver.current_url == 'https://animego.org/anime/status/ongoing' \
           or 'https://animego.org/anime/season/2024' or 'https://animego.org/anime/season/2023'


@allure.title("Test information for copyright holders")
def test_information_elem_footer(driver):
    main_page = MainPage(driver)
    base_page = BasePage(driver)
    main_page.footer_elem()
    assert base_page.get_text(FooterLocators.FOOTER) == "Для правообладателей"


@allure.title("Test reviews")
def test_reviews(driver):
    anime_page = AnimePage(driver)
    base_page = BasePage(driver)
    anime_page.reviews()
    assert base_page.get_locator_xpath(AnimeLocators.WRITE_COMMENTS)


@pytest.mark.xfail(reason="NoSuchElementException, need to log in")
@pytest.mark.parametrize("locator", [AnimeLocators.STATUS_ABANDONED,
                                     AnimeLocators.STATUS_POSTPONED,
                                     AnimeLocators.STATUS_REVIEWED,
                                     AnimeLocators.STATUS_REVIEWING,
                                     AnimeLocators.STATUS_SCHEDULED])
@allure.title("Test choose status")
def test_choose_status(driver, locator):
    anime_page = AnimePage(driver)
    anime_page.status()
    base_page = BasePage(driver)
    base_page.click_on(locator)
    assert base_page.get_text(
        AnimeLocators.TEXT_STATUS) == "Просмотрено" or "Смотрю" or "Отложено" or "Брошено" or "Пересматриваю"
