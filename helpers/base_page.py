import time
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_text(self, xpath):
        element = self.driver.find_element(By.XPATH, xpath)
        return element.text

    def get_attribute(self, locator, attribute):
        element = self.driver.find_element(By.XPATH, locator)
        return element.get_attribute(attribute)

    def get_locator_xpath(self, locator):
        return self.driver.find_element(By.XPATH, locator)

    def click_on(self, locator):
        element = self.get_locator_xpath(locator)
        element.click()

    def click_on_with_text(self, locator):
        element = self.get_locator_link_text(locator)
        element.click()

    def get_locator_css(self, locator):
        return self.driver.find_element(By.CSS_SELECTOR, locator)

    def get_locator_link_text(self, locator):
        return self.driver.find_element(By.LINK_TEXT, locator)

    def click_on_css(self, locator):
        element = self.get_locator_css(locator)
        element.click()

    def send_keys(self, locator, text):
        element = self.driver.find_element(By.XPATH, locator)
        element.send_keys(text)

    def send_keys_css(self, locator, text):
        element = self.driver.find_element(By.CSS_SELECTOR, locator)
        element.send_keys(text)

    def clear_input(self, locator):
        element = self.driver.find_element(By.XPATH, locator)
        element.clear()

    def click_release(self, locator):
        element = self.driver.find_element(By.XPATH, locator)
        ActionChains(self.driver).click(element).perform()

    def keyboard_click(self, locator):
        element = self.driver.find_element(By.XPATH, locator)
        ActionChains(self.driver).key_down(Keys.CONTROL).click(element).key_up(Keys.CONTROL).perform()

    def click_by_js(self, locator):
        element = self.driver.find_element(By.XPATH, locator)
        self.driver.execute_script("arguments[0].click();", element)

    def double_click(self, locator):
        element = self.driver.find_element(By.XPATH, locator)
        ActionChains(self.driver).double_click(element).perform()

    def wait_and_click(self, locator, time_out=10):  # noqa C901
        try:
            element = WebDriverWait(self.driver, time_out).until(
                EC.element_to_be_clickable((By.XPATH, locator))
            ).click()
            return element
        except TimeoutException:
            assert False, f"Element {locator} does not find"

    def wait_for(self, locator, time_out=10):  # noqa C901
        try:
            return WebDriverWait(self.driver, time_out).until(
                EC.element_to_be_clickable((By.XPATH, locator))
            )
        except TimeoutException:
            assert False, f'Element {locator} doesnt found'

    def wait_another_url(self, url):  # noqa C901
        if self.driver.current_url == url:
            time.sleep(5)
        else:
            return False

    def scroll_to(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

    def move_to_element(self, locator, timeout=15):
        element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, locator)))
        ActionChains(self.driver).move_to_element(element).click().perform()
