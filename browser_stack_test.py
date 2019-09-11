from selenium import webdriver
import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


@pytest.fixture
def browser(request):
    desired_cap = {
        'browser': 'Chrome',
        'browser_version': '62.0',
        'os': 'Windows',
        'os_version': '10',
        'resolution': '1024x768',
        'name': 'Bstack-[Python] Sample Test'
    }

    driver = webdriver.Remote(
        command_executor='http://dedtolya1:rnyHhjnPNkPnxiCDDVUr@hub.browserstack.com:80/wd/hub',
        desired_capabilities=desired_cap)
    return driver



def test_one(browser):
    browser.get("http://www.google.com")
    if not "Google" in browser.title:
        raise Exception("Unable to load google page!")
    elem = browser.find_element_by_name("q")
    elem.send_keys("BrowserStack")
    elem.submit()
    print(browser.title)
    browser.quit()
    pass