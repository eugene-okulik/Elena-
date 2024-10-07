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


def test_id_name(driver):
    input_data = 'HelloWorld-1234_test'
    driver.get('https://www.qa-practice.com/elements/input/simple')
    text_string = driver.find_element(By.NAME, 'text_string')
    text_string.send_keys(input_data)
    text_string.send_keys(Keys.ENTER)
    result_text = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, 'result-text'))
    )
    assert result_text.text == input_data
    print(result_text.text)
