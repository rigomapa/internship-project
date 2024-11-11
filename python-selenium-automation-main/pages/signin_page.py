from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class SignInPage(Page):

    HOME_PAGE_URL = "https://soft.reelly.io"
    SIGNIN_PAGE_URL = "https://soft.reelly.io/sign-in"
    EMAIL_INPUT = By.ID, "email-2"
    PASSWORD_INPUT = By.CSS_SELECTOR, 'input[data-name="Password"]'
    CONTINUE_BTN = By.CSS_SELECTOR, 'a.login-button.w-button'
    SIGNIN_HEADER = By.XPATH, '//h1[contains(text(), "Sign in")]'
    USER_EMAIL = "r************************"
    USER_PASSWORD = "***************"

    def open_signin_page(self):
        self.open(self.HOME_PAGE_URL)
        self.wait_for_url(self.SIGNIN_PAGE_URL)
        self.wait_for_element_to_appear(*self.SIGNIN_HEADER)
        sleep(1)

    def enter_username(self):
        self.input_text(*self.EMAIL_INPUT, text=self.USER_EMAIL)

    def enter_password(self):
        self.input_text(*self.PASSWORD_INPUT, text=self.USER_PASSWORD)

    def press_continue_button(self):
        # self.wait_for_element_to_be_clickable(*self.CONTINUE_BTN)
        self.click(*self.CONTINUE_BTN)
        sleep(2)
