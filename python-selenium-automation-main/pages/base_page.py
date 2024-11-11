from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        self.driver.get(url)

    def scroll_down(self):
        self.driver.execute_script("window.scrollBy(0, 500)")

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def get_text(self, *locator):
        return self.driver.find_element(*locator).text

    def click(self, *locator):
        self.find_element(*locator).click()

    def input_text(self, *locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def wait_for_element_to_appear(self, *locator):
        self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_url(self, url):
        self.wait.until(EC.url_to_be(url))

    def wait_for_all_elements_to_appear(self, *locator):
        self.wait.until(EC.visibility_of_all_elements_located(locator))

    def wait_for_element_to_be_clickable(self, *locator):
        self.wait.until(EC.element_to_be_clickable(locator))