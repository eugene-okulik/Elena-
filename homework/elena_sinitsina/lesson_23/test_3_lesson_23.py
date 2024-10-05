from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


def test_student_registration_form(driver):
    input_language = 'Python'
    driver.get('https://www.qa-practice.com/elements/select/single_select')
    language_dropdown = driver.find_element(By.ID, 'id_choose_language')
    language_dropdown.send_keys(input_language, Keys.RETURN)
    driver.find_element(By.ID, 'submit-id-submit').click()

    result = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'result')))

    assert input_language in result.text, f"Expected language '{input_language}' wrong result!"


def test_input_text_form(driver):
    expected_text = 'Hello World!'
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    start_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#start button'))
    )
    start_button.click()

    result = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '#finish h4')))
    assert expected_text == result.text, f"Expected text '{expected_text}' wrong result!"
