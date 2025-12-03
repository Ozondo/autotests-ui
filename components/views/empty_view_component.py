from components.base_component import BaseComponent
from playwright.sync_api import Page, expect
from elements.icon import Icon
from elements.text import Text


class EmptyViewComponent(BaseComponent):

    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.icon = Icon(page,'{identifier}-empty-view-icon', 'Empty View Icon')
        self.title = Text(page,'{identifier}-empty-view-title-text', 'Empty View Title')
        self.description = Text(page,'{identifier}-empty-view-description-text', 'Empty View Description')


    def check_visible(self, title: str, description: str, identifier: str):
        self.icon.check_visible(identifier=identifier)

        self.title.check_visible(identifier=identifier)
        self.title.check_have_text(title, identifier=identifier)

        self.description.check_visible(identifier=identifier)
        self.description.check_have_text(description, identifier=identifier)