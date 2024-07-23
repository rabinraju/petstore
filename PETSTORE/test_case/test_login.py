from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest

@pytest.fixture
def browser():
    driver = webdriver.Chrome()  # Make sure ChromeDriver is in your PATH
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_home_page_title(browser):
    browser.get("https://petstore.octoperf.com/actions/Catalog.action")
    assert "JPetStore Demo" in browser.title

def test_search_for_fish(browser):
    browser.get("https://petstore.octoperf.com/actions/Catalog.action")
    search_box = browser.find_element(By.NAME, "keyword")
    search_box.send_keys("fish" + Keys.RETURN)
    results = browser.find_elements(By.XPATH, "//a[contains(@href, 'Catalog.action?viewItem&itemId=')]")
    assert len(results) > 0

def test_navigate_to_dogs_section(browser):
    browser.get("https://petstore.octoperf.com/actions/Catalog.action")
    dogs_link = browser.find_element(By.XPATH, "//a[contains(text(), 'Dogs')]")
    dogs_link.click()
    assert "Dogs" in browser.page_source







