from playwright.sync_api import Page
import pytest

from pages.courses_list_page import CoursesListPage
from pages.dashboard_page import DashBoardPage
from pages.registration_page import RegistrationPage
from pages.create_course_page import CreateCoursePage


@pytest.fixture
def registration_page(chromium_page_with_state: Page) -> RegistrationPage:
    return RegistrationPage(page=chromium_page_with_state)

@pytest.fixture
def dashboard_page(chromium_page_with_state: Page) -> DashBoardPage:
    return DashBoardPage(page=chromium_page_with_state)

@pytest.fixture
def course_list_page(chromium_page_with_state: Page) -> CoursesListPage:
    return CoursesListPage(page=chromium_page_with_state)

@pytest.fixture
def create_course_page(chromium_page_with_state: Page) -> CreateCoursePage:
    return CreateCoursePage(page=chromium_page_with_state)