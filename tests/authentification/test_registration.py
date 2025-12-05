import pytest

from pages.dashboard.dashboard_page import DashBoardPage
from pages.authentification.registration_page import RegistrationPage


@pytest.mark.registration
@pytest.mark.regression
class TestRegistration:
    def test_successful_registration(self,registration_page: RegistrationPage, dashboard_page: DashBoardPage):
        registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

        registration_page.fill_registration_form(
            email='example@mail.com', username='example_username', password='example_password'
        )

        registration_page.click_registration_button()

        dashboard_page.check_dashboard_title_visible()