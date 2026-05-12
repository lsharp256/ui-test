from playwright.sync_api import Page, expect

SCORES_FIXTURES_URL = "https://www.bbc.co.uk/sport/football/scores-fixtures"
SEARCH_BUTTON_SELECTOR = ".ux-v5"
SEARCH_INPUT_SELECTOR = "#search-input"
RESULT_LINK_SELECTOR = 'a[href^="https://www.bbc.co.uk/programmes/"]'


def test_sports_search(page: Page) -> None:
    page.goto(SCORES_FIXTURES_URL, wait_until="domcontentloaded")

    page.locator(SEARCH_BUTTON_SELECTOR).click()
    search_bar = page.locator(SEARCH_INPUT_SELECTOR)
    expect(search_bar).to_be_visible()

    search_bar.fill("sports")
    search_bar.press("Enter")
    page.wait_for_load_state("networkidle")

    result_links = page.locator(RESULT_LINK_SELECTOR)
    expect(result_links.first).to_be_visible()

    result_count = result_links.count()
    assert result_count > 0
    assert result_links.nth(0).inner_text().strip()
    assert result_links.nth(result_count - 1).inner_text().strip()
