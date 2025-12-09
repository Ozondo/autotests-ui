import re
import allure

from components.base_component import BaseComponent
from playwright.sync_api import Page

from components.navigation.sidebar_list_item_component import SideBarListItemComponent


class SideBarComponent(BaseComponent):

    def __init__(self, page: Page):
        super().__init__(page)

        self.logout_list_item = SideBarListItemComponent(page, identifier="logout")
        self.courses_list_item = SideBarListItemComponent(page, identifier="courses")
        self.dashboard_list_item = SideBarListItemComponent(page, identifier="dashboard")

    @allure.step('Check visible sidebar')
    def check_visible(self):
        self.logout_list_item.check_visible('Logout')
        self.courses_list_item.check_visible('Courses')
        self.dashboard_list_item.check_visible('Dashboard')

    @allure.step('Click logout on sidebar')
    def click_logout(self):
        self.logout_list_item.navigate_url(re.compile(r".*/#/auth/login"))

    @allure.step('Click courses on sidebar')
    def click_courses(self):
        self.logout_list_item.navigate_url(re.compile(r".*/#/courses"))

    @allure.step('Click dashboard on sidebar')
    def click_dashboard(self):
        self.logout_list_item.navigate_url(re.compile(r".*/#/dashboard"))


