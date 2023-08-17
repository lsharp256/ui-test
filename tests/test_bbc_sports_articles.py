def test_sports_search(page):
    # Navigate to the URL
    page.goto("https://www.bbc.com/sport/football/scores-fixtures")

    # Locate the search bar and type 'sports'
    page.locator('.ux-v5').click()
    search_bar = page.locator('#search-input')
    search_bar.fill('sports')
    search_bar.press('Enter')

    # Wait for the search results to load
    page.wait_for_load_state('networkidle')

    # Get the first and last heading from the search results
    links = page.query_selector_all('a[href^="https://www.bbc.co.uk/programmes/"]')
    
    if links:
        first_headline = links[0].inner_text()
        last_headline = links[-1].inner_text()

        print("\n")
        print("First search result:", first_headline)
        print("Last search result:", last_headline)
    else:
        print("No search results found.")
