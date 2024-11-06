from pages.base_page import Page
from pages.signin_page import SignInPage
from pages.offplan_page import OffPlanPage

class Application:

    def __init__(self, driver):
        self.page = Page(driver)
        self.signin_page = SignInPage(driver)
        self.offplan_page = OffPlanPage(driver)