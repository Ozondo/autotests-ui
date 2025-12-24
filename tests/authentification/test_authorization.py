import pytest
import allure

from config import settings
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from allure_commons.types import Severity
from pages.authentification.login_page import LoginPage
from pages.authentification.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashBoardPage
from tools.routes import AppRoute


@pytest.mark.authorization
@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.AUTHORIZATION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.AUTHORIZATION)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.AUTHENTICATION)
@allure.sub_suite(AllureStory.AUTHORIZATION)
class TestAuthorization:
    @allure.title("User login with correct email and password")
    @allure.tag(AllureTag.USER_LOGIN)
    @allure.severity(Severity.BLOCKER)
    @pytest.mark.xdist_group(name="authorization-group")
    def test_successful_authorization(
            self,
            dashboard_page: DashBoardPage,
            registration_page: RegistrationPage,
            login_page: LoginPage,
    ):
        registration_page.visit(AppRoute.REGISTRATION)

        registration_page.registration_form.fill(
            email=settings.test_user.email,
            username=settings.test_user.username,
            password=settings.test_user.password
        )
        registration_page.click_registration_button()

        dashboard_page.dashboard_toolbar.check_visible()
        dashboard_page.navbar.check_visible(settings.test_user.username)
        dashboard_page.sidebar.check_visible()

        dashboard_page.sidebar.click_logout()

        login_page.login_form.fill(
            email=settings.test_user.email,
            password=settings.test_user.password
        )
        login_page.click_login_button()

    @allure.title('User login with wrong email or password')
    @pytest.mark.parametrize('email, password', [('321', '321'), ('4324234', '324234234')])
    @allure.tag(AllureTag.USER_LOGIN)
    @allure.severity(Severity.CRITICAL)
    def test_wrong_email_or_password_authorization(self,login_page: LoginPage, email: str, password: str):
        login_page.visit(AppRoute.LOGIN)
        login_page.check_visible()
        login_page.fill(email=email, password=password)
        login_page.click_login_button()
        login_page.check_alert()

    @allure.title('Navigation from login page to registration page')
    @allure.tag(AllureTag.NAVIGATION)
    @allure.severity(Severity.NORMAL)
    def test_navigate_from_authorization_to_registration(
            self,
            registration_page: RegistrationPage,
            login_page: LoginPage
    ):
        login_page.visit(AppRoute.LOGIN)

        login_page.click_registration_link()

        registration_page.registration_form.check_visible(email='', username='', password='')
