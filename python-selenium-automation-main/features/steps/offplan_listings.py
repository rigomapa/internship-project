from selenium.webdriver.common.by import By
from behave import given, then, when


@given("Open the main page")
def open_main_page(context):
    context.app.signin_page.open_signin_page()


@given("Log in to the page")
def log_in(context):
    context.app.signin_page.sign_in()


@when("Click on “off plan” at the left side menu")
def click_off_plan_side(context):
    context.app.offplan_page.click_off_plan_side_m()


@then("Verify the right page opens")
def verify_off_plan_page(context):
    context.app.offplan_page.verify_off_plan_page()


@then("Verify each product on this page contains a title and picture visible")
def verify_title_and_picture(context):
    context.app.offplan_page.verify_title_and_picture()
