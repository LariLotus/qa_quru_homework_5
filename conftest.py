import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture()
def browser_managment():
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    browser.config.driver_options = chrome_options
    browser.driver.maximize_window()
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.base_url = 'https://demoqa.com'