from pages.customer_login import CustomerLogin


def test_incorrect_email(page):
    login_page = CustomerLogin(page)
    login_page.open_page()
    login_page.fill_login_form(
        'Aaa',"Bb","111@11","Amari648377","Amari648377"
    )
    login_page.check_error_alert_text_is(
        'Please enter a valid email address (Ex: johndoe@domain.com).'
    )

def test_incorrect_password(page):
    login_page = CustomerLogin(page)
    login_page.open_page()
    login_page.fill_login_form(
        "Aaa","Bb","123@gmail.com","Amari648377","123"
    )
    login_page.check_error_alert_incorrect_password_is(
        'Please enter the same value again.'
    )

def test_weak_password(page):
    login_page = CustomerLogin(page)
    login_page.open_page()
    login_page.fill_login_form(
        "Aaa", "Bb", "123@gmail.com", "123", "123"
    )
    login_page.check_error_alert_weak_password_is(
        'Minimum length of this field must be equal or greater than 8 symbols. '
                                'Leading and trailing spaces will be ignored.'
    )
