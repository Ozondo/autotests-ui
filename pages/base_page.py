from playwright.sync_api import Page, expect
import allure
from typing import Pattern
from tools.playwright.logger import get_logger


logger = get_logger('BASE_PAGE')

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def visit(self, url: str):
        step = f'Visit "{url}"'
        with allure.step(step):
            logger.info(step)
            self.page.goto(url)

    def reload(self):
        step = 'Reload page'
        with allure.step(step):
            logger.info(step)
            self.page.reload()

    def check_current_url(self, expected_url: Pattern[str]):
        step = f'Checking that current url matches pattern "{expected_url.pattern}"'
        with allure.step(step):
            logger.info(step)
            expect(self.page).to_have_url(expected_url)