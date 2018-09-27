from selenium import webdriver


def before_all(context):
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(10)


def after_all(context):
    context.driver.quit()
