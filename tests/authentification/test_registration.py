import pytest
import allure

from pages.dashboard.dashboard_page import DashBoardPage
from pages.authentification.registration_page import RegistrationPage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from allure_commons.types import Severity


@pytest.mark.registration
@pytest.mark.regression
@allure.tag(AllureTag.REGISTRATION, AllureTag.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.REGISTRATION)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.AUTHENTICATION)
@allure.sub_suite(AllureStory.REGISTRATION)
class TestRegistration:
    @allure.severity(Severity.CRITICAL)
    @allure.title('Registration with correct email, username and password')
    def test_successful_registration(self,registration_page: RegistrationPage, dashboard_page: DashBoardPage):
        registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

        registration_page.fill_registration_form(
            email='example@mail.com', username='example_username', password='example_password'
        )

        registration_page.click_registration_button()

        dashboard_page.check_dashboard_title_visible()