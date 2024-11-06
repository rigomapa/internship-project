from selenium.webdriver.common.by import By


from pages.base_page import Page


class SignInPage(Page):

    SIGNIN_PAGE_URL = "https://soft.reelly.io"
    EMAIL_INPUT = By.ID, "email-2"
    PASSWORD_INPUT = By.CSS_SELECTOR, 'input[data-name="Password"]'
    CONTINUE_BTN = By.CSS_SELECTOR, 'a.login-button.w-button'
    SIGNIN_HEADER = By.XPATH, '//h1[contains(text(), "Sign in")]'
    USER_EMAIL = "r************************"
    USER_PASSWORD = "**************"

    def open_signin_page(self):
        self.open(self.SIGNIN_PAGE_URL)
        self.wait_for_element_to_appear(*self.SIGNIN_HEADER)

    def sign_in(self):
        self.input_text(*self.EMAIL_INPUT, text=self.USER_EMAIL)
        self.input_text(*self.PASSWORD_INPUT, text=self.USER_PASSWORD)
        self.click(*self.CONTINUE_BTN)
