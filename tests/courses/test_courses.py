import pytest
import allure

from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage
from tools.tags import AllureTag
from tools.epics import AllureEpic
from tools.features import AllureFeature
from tools.stories import AllureStory
from allure_commons.types import Severity


@pytest.mark.courses
@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.COURSES)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.COURSES)
@allure.story(AllureStory.COURSES)
class TestCourses:
    @allure.severity(Severity.CRITICAL)
    @allure.title("Create course")
    def test_create_course(self,course_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        create_course_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')

        create_course_page.check_visible_create_course_title(is_create_course_disabled=True)
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)
        create_course_page.check_visible_create_course_form(
            title='',
            estimated_time='',
            description='',
            max_score='0',
            min_score='0',
        )
        create_course_page.create_course_exercises_toolbar.check_visible()
        create_course_page.check_visible_exercises_empty_view()

        create_course_page.image_upload_widget.upload_preview_image(file='test_data/files/image.png')
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)

        create_course_page.fill_create_course_form(
            title="Playwright",
            estimated_time='2 weeks',
            description='Playwright',
            max_score='100',
            min_score='10',
        )

        create_course_page.click_create_course_button()

        course_list_page.toolbar_view.check_visible()

        course_list_page.course_view.check_visible(
            index=0,
            title='Playwright',
            estimated_time='2 weeks',
            max_score='100',
            min_score='10',
        )

    @allure.title('Check displaying of empty courses list')
    @allure.severity(Severity.NORMAL)
    def test_empty_courses_list(self,course_list_page: CoursesListPage):
        course_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        course_list_page.navbar.check_visible(username='username')
        course_list_page.sidebar.check_visible()

        course_list_page.toolbar_view.check_visible()
        course_list_page.check_visible_empty_view()

    @allure.severity(Severity.NORMAL)
    def test_edit_course(self, create_course_page: CreateCoursePage, course_list_page: CoursesListPage):
        create_course_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')

        create_course_page.create_course_form.fill(
            title='Playwright',
            estimated_time='2 weeks',
            description='Playwright',
            max_score='100',
            min_score='10',
        )

        create_course_page.image_upload_widget.upload_preview_image(file='test_data/files/image.png')

        create_course_page.click_create_course_button()

        course_list_page.course_view.check_visible(
            index=0,
            title='Playwright',
            estimated_time='2 weeks',
            max_score='100',
            min_score='10',
        )

        course_list_page.course_view.menu.click_edit(index=0)

        create_course_page.create_course_form.fill(
            title='Python',
            estimated_time='1 hour',
            description='Python',
            max_score='10',
            min_score='1',
        )

        create_course_page.click_create_course_button()

        course_list_page.course_view.check_visible(
            index=0,
            title='Python',
            estimated_time='1 hour',
            max_score='10',
            min_score='1',
        )