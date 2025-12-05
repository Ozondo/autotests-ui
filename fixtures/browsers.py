from typing import Any, Generator

from playwright.sync_api import Playwright, Page
import pytest

from pages.authentification.registration_page import RegistrationPage


@pytest.fixture(scope='session')
def initialize_browser_state(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    page = context.new_page()

    registration_page = RegistrationPage(page)
    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    registration_page.registration_form.fill(email='user.name@gmail.com',username='username',password='password')
    registration_page.click_registration_button()

    context.storage_state(path='browser-state.json')

    context.close()

@pytest.fixture
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Generator[Page, Any, None]:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json')
    page = context.new_page()

    yield page

    page.close()

@pytest.fixture
def chromium_page(playwright: Playwright) -> Generator[Page, Any, None]:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    yield page

    browser.close()