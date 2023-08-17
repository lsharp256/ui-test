def test_bbc_football_fixtures(page):
    page.goto('https://www.bbc.co.uk/sport/football/scores-fixtures')

    # Wait for the specific selector to be visible on the page
    page.wait_for_selector('.qa-full-team-name')

    # Extracting team names
    fixtures = page.query_selector_all('.sp-c-fixture')
    total_teams_playing = len(fixtures) * 2

    assert fixtures, "No matches today."

    print('\n')
    print('-----------------------')
    print('Teams playing today:')
    print('-----------------------')
    print('\n')
    for fixture in fixtures:
        home_team = fixture.query_selector('.sp-c-fixture__team-name--home').inner_text()
        away_team = fixture.query_selector('.sp-c-fixture__team-name--away').inner_text()
        
        print(f'{home_team} vs {away_team}')

    print('-----------------------')
    print(f'Total number of teams playing today: {total_teams_playing}')
