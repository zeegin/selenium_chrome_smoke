from behave import step
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@step('I goto {url}')
def step_impl(context, url):
    context.driver.get(url)


@step('I enter user name {username}')
def step_impl(context, username):

    context.driver\
        .find_element_by_id("userName")\
        .send_keys(username)

    context.driver\
        .find_element_by_id("userPassword")\
        .send_keys(Keys.RETURN)


@step('I wait until the title contains {fragment}')
def step_impl(context, fragment):

    wait = WebDriverWait(context.driver, 15)
    wait.until(EC.title_contains(fragment))


@step("I wait until home page is opened")
def step_impl(context):
    wait = WebDriverWait(context.driver, 15)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'openedHomeTitle')))


@step("I take screenshot to {file}")
def step_impl(context, file):

    context.driver.get_screenshot_as_file(file)
