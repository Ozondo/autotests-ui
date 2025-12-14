import pytest
import allure

from pages.dashboard.dashboard_page import DashBoardPage
from pages.authentification.registration_page import RegistrationPage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from allure_commons.types import Severity

from tools.routes import AppRoute
from config import settings


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
        registration_page.visit(AppRoute.REGISTRATION)

        registration_page.fill_registration_form(
            email=settings.test_user.email,
            username=settings.test_user.username,
            password=settings.test_user.password
        )

        registration_page.click_registration_button()

        dashboard_page.check_dashboard_title_visible()