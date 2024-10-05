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
    input_name = 'Sherlock'
    input_last_name = 'Holmes'
    input_email = 'sherlock@example.com'
    input_gender = 'Male'
    input_user_number = '9999999999'
    input_date_birth = '03 Oct 1980'
    input_subject = 'Math'
    input_hobby = 'Music'
    input_upload_picture = r'D:\My documents Elena\Elena-\homework\elena_sinitsina\lesson_23\Sherlock_H.jpg'
    input_current_address = '221B Baker Street'

    driver.get('https://demoqa.com/automation-practice-form')

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'firstName')))

    driver.find_element(By.ID, 'firstName').send_keys(input_name)
    driver.find_element(By.ID, 'lastName').send_keys(input_last_name)
    driver.find_element(By.ID, 'userEmail').send_keys(input_email)
    driver.find_element(By.ID, 'userNumber').send_keys(input_user_number)
    driver.find_element(By.ID, 'currentAddress').send_keys(input_current_address)

    driver.find_element(By.XPATH, "//label[text()='{}']".format(input_gender)).click()

    date_of_birth_field = driver.find_element(By.ID, 'dateOfBirthInput')
    date_of_birth_field.clear()
    date_of_birth_field.send_keys(input_date_birth)
    date_of_birth_field.send_keys(Keys.RETURN)

    subjects_input = driver.find_element(By.ID, 'subjectsInput')
    subjects_input.send_keys(input_subject)
    subjects_input.send_keys(Keys.RETURN)

    driver.find_element(By.XPATH, "//label[text()='{}']".format(input_hobby)).click()

    driver.find_element(By.ID, 'uploadPicture').send_keys(input_upload_picture)

    driver.find_element(By.ID, 'react-select-3-input').send_keys('NCR', Keys.RETURN)
    driver.find_element(By.ID, 'react-select-4-input').send_keys('Gurgaon', Keys.RETURN)

    driver.find_element(By.ID, 'submit').click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Thanks for submitting the form')]"))
    )

    success_message = driver.find_element(By.XPATH, "//div[contains(text(),'Thanks for submitting the form')]")
    assert success_message.is_displayed(), "Success message not displayed!"
