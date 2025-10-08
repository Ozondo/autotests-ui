from playwright.sync_api import sync_playwright, expect



with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    registration_email_input = page.locator('//div[@data-testid="registration-form-email-input"]//div//input')
    registration_email_input.fill('user.name@gmail.com')

    registration_username = page.locator('//div[@data-testid="registration-form-username-input"]//div//input')
    registration_username.fill('username')

    registration_password = page.locator('//div[@data-testid="registration-form-password-input"]//div//input')
    registration_password.fill('password')

    registration_button = page.locator('//button[@data-testid="registration-page-registration-button"]')
    registration_button.click()

    dashboard_element = page.locator('//h6[@data-testid="dashboard-toolbar-title-text"]')

    expect(dashboard_element).to_be_visible()

