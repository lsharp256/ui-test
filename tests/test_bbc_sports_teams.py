from playwright.sync_api import Page, expect

SCORES_FIXTURES_URL = "https://www.bbc.co.uk/sport/football/scores-fixtures"
FIXTURE_SELECTOR = ".sp-c-fixture"
TEAM_NAME_SELECTOR = ".qa-full-team-name"


def test_bbc_football_fixtures(page: Page) -> None:
    page.goto(SCORES_FIXTURES_URL, wait_until="domcontentloaded")

    fixtures = page.locator(FIXTURE_SELECTOR)
    expect(fixtures.first).to_be_visible()

    fixture_count = fixtures.count()
    assert fixture_count > 0, "No matches today."

    team_names = []
    for fixture_index in range(fixture_count):
        teams = fixtures.nth(fixture_index).locator(TEAM_NAME_SELECTOR)
        expect(teams.first).to_be_visible()

        visible_team_count = teams.count()
        assert visible_team_count >= 2

        home_team = teams.nth(0).inner_text().strip()
        away_team = teams.nth(1).inner_text().strip()
        assert home_team
        assert away_team
        team_names.extend((home_team, away_team))

    assert len(team_names) == fixture_count * 2
