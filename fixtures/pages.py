from playwright.sync_api import Page
import pytest

from pages.dashboard_page import DashBoardPage
from pages.registration_page import RegistrationPage


@pytest.fixture
def registration_page(chromium_page: Page):
    return RegistrationPage(page=chromium_page)

@pytest.fixture
def dashboard_page(chromium_page: Page):
    return DashBoardPage(page=chromium_page)