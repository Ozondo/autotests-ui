import re

from components.base_component import BaseComponent
from playwright.sync_api import Page

from components.navigation.sidebar_list_item_component import SideBarListItemComponent


class SideBarComponent(BaseComponent):

    def __init__(self, page: Page):
        super().__init__(page)

        self.logout_list_item = SideBarListItemComponent(page)
        self.courses_list_item = SideBarListItemComponent(page)
        self.dashboard_list_item = SideBarListItemComponent(page)


    def check_visible(self):
        self.logout_list_item.check_visible('Logout', identifier='logout')
        self.courses_list_item.check_visible('Courses', identifier='courses')
        self.dashboard_list_item.check_visible('Dashboard', identifier='dashboard')

    def click_logout(self):
        self.logout_list_item.navigate_url(re.compile(r".*/#/auth/login"))

    def click_courses(self):
        self.logout_list_item.navigate_url(re.compile(r".*/#/courses"))

    def click_dashboard(self):
        self.logout_list_item.navigate_url(re.compile(r".*/#/dashboard"))


