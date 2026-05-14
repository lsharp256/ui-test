import pytest
from playwright.sync_api import Page, expect

USERNAME_INPUT_SELECTOR = "#user-identifier-input"
PASSWORD_INPUT_SELECTOR = "#password-input"
SUBMIT_BUTTON_SELECTOR = "#submit-button"
ERROR_SELECTORS = (
    "#form-message-username",
    "#form-message-password",
    ".form-message--general",
)

SCENARIOS = [
    ("", "", "Something's missing. Please check and try again."),
    ("", "valid_password", "Something's missing. Please check and try again."),
    (
        "valid_username",
        "12312",
        "Sorry, that password is too short. It needs to be eight characters or more.",
    ),
    (
        "valid_username",
        "asdasdasdasdasdasd",
        "Sorry, that password isn't valid. Please include something that isn't a letter.",
    ),
    (
        "valid_username",
        "12312,./,.",
        "Sorry, that password isn't valid. Please include a letter.",
    ),
    (
        "incorrect_username",
        "incorrect_password",
        "Looks like either the email/username or password is wrong. Try again, reset your password or get help.",
    ),
    (
        "bad@@email.com",
        "",
        "Sorry, that email doesn’t look right. Please check it's a proper email.",
    ),
    (
        "bad@email",
        "",
        "Sorry, that email doesn’t look right. Please check it's a proper email.",
    ),
]


def get_visible_error_message(page: Page) -> str:
    page.wait_for_selector(", ".join(ERROR_SELECTORS))

    for selector in ERROR_SELECTORS:
        error_message = page.locator(selector)
        if error_message.is_visible():
            return error_message.inner_text().strip()

    raise AssertionError("No login error message was displayed.")


@pytest.mark.parametrize(("username", "password", "expected_error"), SCENARIOS)
def test_login_negative_scenarios(
    scores_fixtures_page: Page, username: str, password: str, expected_error: str
) -> None:
    page = scores_fixtures_page
    page.locator("#idcta-username").click()

    page.locator(USERNAME_INPUT_SELECTOR).fill(username)
    page.locator(PASSWORD_INPUT_SELECTOR).fill(password)
    page.locator(SUBMIT_BUTTON_SELECTOR).click()

    assert get_visible_error_message(page) == expected_error
    expect(page.locator(USERNAME_INPUT_SELECTOR)).to_be_visible()
