def test_bbc_football_fixtures(page):
    page.goto('https://www.bbc.co.uk/sport/football/scores-fixtures')

    line = '-----------------------' * 3
    # Wait for the specific selector to be visible on the page
    page.wait_for_selector('.qa-full-team-name')

    # Extracting team names
    fixtures = page.query_selector_all('.sp-c-fixture')
    total_teams_playing = len(fixtures) * 2

    assert fixtures, "No matches today."

    print('\n')
    print(line)
    print('Teams playing today:')
    print(line)
    print('\n')

    # Looping through the fixtures and displaying the teams
    for fixture in fixtures:
        teams = fixture.query_selector_all('.qa-full-team-name')
        home_team = teams[0].inner_text() if teams and len(teams) > 0 else None
        away_team = teams[1].inner_text() if teams and len(teams) > 1 else None

        if home_team and away_team:
            print(f'{home_team} vs {away_team}')


    print(line)
    print(f'Total number of teams playing today: {total_teams_playing}')
