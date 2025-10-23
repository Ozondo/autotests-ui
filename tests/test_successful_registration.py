import pytest

from pages.dashboard_page import DashBoardPage
from pages.registration_page import RegistrationPage

@pytest.mark.registration
@pytest.mark.regression
def test_successful_registration(registration_page: RegistrationPage, dashboard_page: DashBoardPage):
    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')


    registration_page.fill_registration_form(
        email='example@mail.com',username='example_username',password='example_password'
    )

    registration_page.click_registration_button()

    dashboard_page.check_dashboard_title_visible()