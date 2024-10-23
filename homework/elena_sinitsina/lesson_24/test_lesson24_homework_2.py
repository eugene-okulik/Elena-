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

def test_add_to_compare(driver):
    driver.get('https://magento.softwaretestingboard.com/gear/bags.html')
    first_product =driver.find_element(By.XPATH, "//img[@alt='Push It Messenger Bag']")
    add_to_compare_button = driver.find_element(By.XPATH, "//a[@title='Add to Compare' and @role='button']")
    actions = ActionChains(driver)
    actions.move_to_element(first_product)
    actions.click(add_to_compare_button)
    actions.perform()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='block block-compare']"))
    )
    compare_product_image = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        "//img[@src='https://magento."
                                        "softwaretestingboard.com/pub/media/catalog/product/cache/"
                                        "7c4c1ed835fbbf2269f24539582c6d44/w/b/wb04-blue-0.jpg']"))
    )
    assert compare_product_image is not None, "The product was not added to the Compare section"
