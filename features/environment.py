from behave import fixture, use_fixture
from selenium import webdriver
from features.configuration.configuration import Configuration


@fixture
def selenium_browser(context):
    # -- HINT: @behave.fixture is similar to @contextlib.contextmanager
    config = Configuration()
    if config.getBrowserType() == "FIREFOX":
        context.browser = webdriver.Firefox()
        context.browser.maximize_window()
        context.browser.delete_all_cookies()
    yield context.browser
    # -- CLEANUP-FIXTURE PART:
    context.browser.quit()


def before_all(context):
    use_fixture(selenium_browser, context)