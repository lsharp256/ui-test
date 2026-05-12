import pytest
from playwright.sync_api import Error, Page

SCORES_FIXTURES_URL = "https://www.bbc.co.uk/sport/football/scores-fixtures"
UNAVAILABLE_NETWORK_ERRORS = (
    "ERR_NAME_NOT_RESOLVED",
    "ERR_INTERNET_DISCONNECTED",
    "ERR_CONNECTION_TIMED_OUT",
)


@pytest.fixture
def scores_fixtures_page(page: Page) -> Page:
    try:
        page.goto(SCORES_FIXTURES_URL, wait_until="domcontentloaded")
    except Error as error:
        if any(network_error in str(error) for network_error in UNAVAILABLE_NETWORK_ERRORS):
            pytest.skip(f"BBC Sport is unavailable from this environment: {error}")
        raise

    return page
