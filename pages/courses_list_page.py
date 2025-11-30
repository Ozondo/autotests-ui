from components.courses.course_view_component import CourseViewComponent
from components.navigation.navbar_component import NavBarComponent
from components.navigation.sidebar_component import SideBarComponent
from components.views.empty_view_component import EmptyViewComponent
from components.courses.courses_list_toolbar_view_component import CoursesListToolbarViewComponent
from pages.base_page import BasePage
from playwright.sync_api import Page, expect


class CoursesListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.empty_view = EmptyViewComponent(page=page, identifier='courses-list')
        self.course_view = CourseViewComponent(page=page)
        self.sidebar = SideBarComponent(page=page)
        self.navbar = NavBarComponent(page=page)
        self.toolbar_view = CoursesListToolbarViewComponent(page=page)


    def check_visible_empty_view(self):
        self.empty_view.check_visible(
            title="There is no results",
            description="Results from the load test pipeline will be displayed here",
        )


