import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture()
def browser_managment():
    # chrome_options = webdriver.ChromeOptions()
    # browser.config.driver_options = chrome_options
    browser.config.base_url = 'https://demoqa.com'
    # browser.driver.maximize_window()
    browser.config.window_width = 1920
    browser.config.window_height = 1080

