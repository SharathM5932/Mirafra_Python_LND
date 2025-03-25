import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_website_navigation(driver):
    driver.get('https://abhijithchandradas.medium.com/')
    assert driver.title == "Abhijith Chandradas – Medium"

#Check for a Specific Element on the Page
def test_check_for_element(driver):
    driver.get('https://abhijithchandradas.medium.com/')
    element = driver.find_element(By.XPATH, "//h1[text()='Abhijith Chandradas']")
    assert element.is_displayed()  # Check if the heading is displayed

#Check for a Link Navigation
def test_check_link_navigation(driver):
    driver.get('https://abhijithchandradas.medium.com/')
    link = driver.find_element(By.LINK_TEXT, "About Me")
    link.click()
    assert driver.title == "About Me – Abhijith Chandradas"  # Check if the title changes

#Check for Image Presence
def test_check_image_presence(driver):
    driver.get('https://abhijithchandradas.medium.com/')
    image = driver.find_element(By.TAG_NAME, "img")
    assert image.is_displayed()  # Check if the first image on the page is displayed


#Verify the Page Loads Within a Timeout
#sometimes passes 60%
def test_page_load_timeout(driver):
    driver.get('https://abhijithchandradas.medium.com/')
    WebDriverWait(driver, 10).until(EC.title_contains("Abhijith Chandradas"))
    assert driver.title == "Abhijith Chandradas – Medium"


def test_follow_button_click(driver):
    driver.get('https://abhijithchandradas.medium.com/')
    follow_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Follow']"))
    )
    follow_button.click()
    # Verify that the button action triggered the expected result (like changing text or state)
    assert follow_button.text == "Following"  # Example assertion, adapt to actual behavior
