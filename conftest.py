import pytest
from selene import browser



@pytest.fixture()
def browser_managment():
    browser.config.base_url = 'https://demoqa.com'

    browser.config.window_width = 1920
    browser.config.window_height = 1080

