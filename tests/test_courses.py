from playwright.sync_api import sync_playwright, expect



def test_empty_courses_list():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()

        page = context.new_page()

        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

        registration_email = page.get_by_test_id('registration-form-email-input').locator('input')
        registration_email.fill('user.name@gmail.com')

        registration_username = page.get_by_test_id('registration-form-username-input').locator('input')
        registration_username.fill('username')

        registration_password = page.get_by_test_id('registration-form-password-input').locator('input')
        registration_password.fill('password')

        registration_button = page.locator('//button[@data-testid="registration-page-registration-button"]')
        registration_button.click()

        context.storage_state(path='browser-state.json')

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state='browser-state.json')

        page = context.new_page()

        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

        heading_element = page.get_by_test_id('courses-list-toolbar-title-text')
        expect(heading_element).to_have_text('Courses')

        icon_element = page.get_by_test_id('courses-list-empty-view-icon')
        expect(icon_element).to_be_visible()

        result_title_element = page.get_by_test_id('courses-list-empty-view-title-text')
        expect(result_title_element).to_have_text('There is no results')

        result_text_element = page.get_by_test_id('courses-list-empty-view-description-text')
        expect(result_text_element).to_have_text('Results from the load test pipeline will be displayed here')