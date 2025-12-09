from playwright.sync_api import Page, expect
import allure

from components.base_component import BaseComponent
from typing import Pattern
from elements.icon import Icon
from elements.button import Button
from elements.text import Text

class SideBarListItemComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.icon = Icon(page,f'{identifier}-drawer-list-item-icon', 'SideBar icon')
        self.title = Text(page,f'{identifier}-drawer-list-item-title-text', 'SideBar title')
        self.button = Button(page,f'{identifier}-drawer-list-item-button', 'SideBar button')

    @allure.step('Check visible "{title}" sidebar list item')
    def check_visible(self, title: str):
        self.icon.check_visible()

        self.title.check_visible()
        self.title.check_have_text(text=title)

        self.button.check_visible()

    def navigate_url(self, expected_url: Pattern[str]):
        self.button.click()
        expect(self.page).to_have_url(expected_url)