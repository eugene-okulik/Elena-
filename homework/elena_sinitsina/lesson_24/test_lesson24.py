from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


def test_add_item_to_cart(driver):
    driver.get('https://www.demoblaze.com/index.html')
    item_link = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//a[text()='Samsung galaxy s6']"))
    )
    ActionChains(driver).key_down(Keys.CONTROL).click(item_link).key_up(Keys.CONTROL).perform()

    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    add_to_cart_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[@onclick='addToCart(1)']"))
    )
    add_to_cart_button.click()
    sleep(5)
    alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert.accept()

    driver.close()
    driver.switch_to.window(tabs[0])

    driver.find_element(By.ID, 'cartur').click()
    cart_item = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//td[contains(text(), 'Samsung galaxy s6')]"))
    )
    assert cart_item is not None, "Samsung galaxy s6 not found in the cart"
