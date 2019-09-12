import pytest
from selenium.webdriver.common import desired_capabilities
from selenium import webdriver

@pytest.fixture
def firefox_browser(request):
    selenium_grid_url = "http://192.168.0.10:13666/wd/hub"
    # Create a desired capabilities object as a starting point.
    capabilities = desired_capabilities.DesiredCapabilities.FIREFOX.copy()
    capabilities['browserName'] = "firefox"
    print(capabilities)
    wd = webdriver.Remote(desired_capabilities=capabilities,
                              command_executor=selenium_grid_url)
    request.addfinalizer(wd.quit)
    return wd

@pytest.fixture
def chrome_browser(request):
    selenium_grid_url = "http://192.168.0.10:13666/wd/hub"
    # Create a desired capabilities object as a starting point.
    capabilities = desired_capabilities.DesiredCapabilities.CHROME.copy()
    capabilities['browserName'] = "chrome"
    print(capabilities)
    wd = webdriver.Remote(desired_capabilities=capabilities,
                              command_executor=selenium_grid_url)
    request.addfinalizer(wd.quit)
    return wd

def test_fxgoogle(firefox_browser):
    firefox_browser.get("http://www.google.com")
    if not "Google" in firefox_browser.title: raise Exception("Unable to load google page!")
    elem = firefox_browser.find_element_by_name("q")
    elem.click()

def test_chrgoogle(chrome_browser):
    chrome_browser.get("http://www.google.com")
    if not "Google" in chrome_browser.title: raise Exception("Unable to load google page!")
    elem = chrome_browser.find_element_by_name("q")
    elem.click()