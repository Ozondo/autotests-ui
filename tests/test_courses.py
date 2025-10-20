import pytest
from playwright.sync_api import expect, Page


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
    chromium_page_with_state.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    heading_element = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(heading_element).to_have_text('Courses')

    icon_element = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(icon_element).to_be_visible()

    result_title_element = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(result_title_element).to_have_text('There is no results')

    result_text_element = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(result_text_element).to_have_text('Results from the load test pipeline will be displayed here')
