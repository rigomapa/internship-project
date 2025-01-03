from selenium.webdriver.common.by import By


from pages.base_page import Page
from time import sleep


class OffPlanPage(Page):

    PAGE_URL = "https://soft.reelly.io"
    OFFPLAN_SIDE_M = By.CSS_SELECTOR, ".menu-text-link-leaderboard.w--current"
    PAGE_TITLE = By.CSS_SELECTOR, 'div.page-title.off_plan'
    LISTING_TITLE = By.CSS_SELECTOR, 'div.project-name'
    LISTING_PICTURE = By.CSS_SELECTOR, 'div.project-image'
    LISTING_CONTAINER = By.CSS_SELECTOR, 'div.cards-properties'
    PROMOTION_POPUP = By.CSS_SELECTOR, ".pop-up-contact-block "
    POPUP_CLOSE_BTN = By.CSS_SELECTOR, ".button-grey.w-inline-block"

    def close_popup(self):
        self.wait_for_element_to_appear(*self.PROMOTION_POPUP)
        self.wait_for_element_to_be_clickable_click(*self.POPUP_CLOSE_BTN)

    def click_off_plan_side_m(self):
        self.wait_for_element_to_be_clickable(*self.OFFPLAN_SIDE_M)
        self.click(*self.OFFPLAN_SIDE_M)

    def verify_off_plan_page(self):
        self.wait_for_element_to_appear(*self.PAGE_TITLE)

    def verify_title_and_picture(self):
        self.wait_for_all_elements_to_appear(*self.LISTING_CONTAINER)
        num_project_titles = self.find_elements(*self.LISTING_TITLE)
        num_project_images = self.find_elements(*self.LISTING_PICTURE)
        assert len(num_project_titles) == len(num_project_images), (f"The total number of project titles does not equal"
                                                                    f"the total number of picture images.")