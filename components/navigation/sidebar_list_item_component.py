from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from typing import Pattern
from elements.icon import Icon
from elements.button import Button
from elements.text import Text

class SideBarListItemComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.icon = Icon(page,'{identifier}-drawer-list-item-icon', 'SideBar icon')
        self.title = Text(page,'{identifier}-drawer-list-item-title-text', 'SideBar title')
        self.button = Button(page,'{identifier}-drawer-list-item-button', 'SideBar button')

    def check_visible(self, title: str, identifier: str):
        self.icon.check_visible(identifier=identifier)

        self.title.check_visible(identifier=identifier)
        self.title.check_have_text(text=title, identifier=identifier)

        self.button.check_visible(identifier=identifier)

    def navigate_url(self, expected_url: Pattern[str]):
        self.button.click()
        expect(self.page).to_have_url(expected_url)