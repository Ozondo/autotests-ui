from playwright.sync_api import Page
import pytest

from pages.courses.courses_list_page import CoursesListPage
from pages.dashboard.dashboard_page import DashBoardPage
from pages.authentification.login_page import LoginPage
from pages.authentification.registration_page import RegistrationPage
from pages.courses.create_course_page import CreateCoursePage

@pytest.fixture
def login_page(chromium_page: Page) -> LoginPage:
    return LoginPage(page=chromium_page)


@pytest.fixture
def registration_page(chromium_page: Page) -> RegistrationPage:
    return RegistrationPage(page=chromium_page)

@pytest.fixture
def dashboard_page(chromium_page: Page) -> DashBoardPage:
    return DashBoardPage(page=chromium_page)

@pytest.fixture
def dashboard_page_with_state(chromium_page_with_state: Page) -> DashBoardPage:
    return DashBoardPage(page=chromium_page_with_state)

@pytest.fixture
def course_list_page(chromium_page_with_state: Page) -> CoursesListPage:
    return CoursesListPage(page=chromium_page_with_state)

@pytest.fixture
def create_course_page(chromium_page_with_state: Page) -> CreateCoursePage:
    return CreateCoursePage(page=chromium_page_with_state)
