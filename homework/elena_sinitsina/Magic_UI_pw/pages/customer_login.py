
from utils import project_ec
from pages.base_page import BasePage
from pages.locators import login_locators as loc


class CustomerLogin(BasePage):

    page_url = "customer/account/create/"

    def fill_login_form(self, firstname, lastname, email, password, password_conf):
        firstname_field = self.find(loc.firstname_field_loc)
        lastname_field = self.find(loc.lastname_field_loc)
        email_field = self.find(loc.email_field_loc)
        password_field = self.find(loc.password_field_loc)
        confirm_password_field = self.find(loc.confirm_password_field_loc )
        button = self.find(loc.button_loc)

        firstname_field.fill(firstname)
        lastname_field.fill(lastname)
        email_field.fill(email)
        password_field.fill(password)
        confirm_password_field.fill(password_conf)
        button.click()


    def check_error_alert_text_is(self,text):
        error_alert = "#email_address-error"
        self.page.wait_for_selector(error_alert, timeout=5000)
        alert_text = self.page.locator(error_alert).inner_text()
        assert alert_text == text, f"Expected '{text}', but got '{alert_text}'"

    def check_error_alert_incorrect_password_is(self,password):
        error_alert = "#password-confirmation-error"
        self.page.wait_for_selector(error_alert, timeout=5000)
        alert_text = self.page.locator(error_alert).inner_text()
        assert alert_text == password, f"Expected '{password}', but got '{alert_text}'"

    def check_error_alert_weak_password_is(self,password):
        error_alert = "#password-error"
        self.page.wait_for_selector(error_alert, timeout=5000)
        alert_text = self.page.locator(error_alert).inner_text()
        assert alert_text == password, f"Expected '{password}', but got '{alert_text}'"
