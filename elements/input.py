import allure
from playwright.sync_api import expect, Locator

from elements.base_element import BaseElement
from tools.playwright.logger import get_logger

logger = get_logger('INPUT')

class Input(BaseElement):

    @property
    def type_of(self) -> str:
        return 'input'

    def get_locator(self,nth: int = 0, **kwargs) -> Locator:
        return super().get_locator(nth,**kwargs).locator('input')

    def fill(self, value: str,nth: int = 0, **kwargs):
        step = f'Filling {self.type_of} {self.name} to value "{value}"'
        with allure.step(step):
            logger.info(step)
            locator = self.get_locator(nth,**kwargs)
            locator.fill(value)

    def check_value(self, value: str,nth: int = 0, **kwargs):
        step = f'Checking {self.type_of} {self.name} has a value "{value}"'
        with allure.step(step):
            logger.info(step)
            locator = self.get_locator(nth,**kwargs)
            expect(locator).to_have_value(value)
