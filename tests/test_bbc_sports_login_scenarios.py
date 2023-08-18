def test_login_negative_scenarios(page):
    page.goto('https://www.bbc.co.uk/sport/football/scores-fixtures')

    # Click on the 'Sign in' button
    page.locator('#idcta-username').click()

    # Negative scenarios to test
    scenarios = [
        {'username': '', 'password': '', 'expected_error': "Something's missing. Please check and try again."},
        {'username': '', 'password': 'valid_password', 'expected_error': "Something's missing. Please check and try again."},
        {'username': 'valid_username', 'password': '12312', 'expected_error': "Sorry, that password is too short. It needs to be eight characters or more."},
        {'username': 'valid_username', 'password': 'asdasdasdasdasdasd', 'expected_error': "Sorry, that password isn't valid. Please include something that isn't a letter."},
        {'username': 'valid_username', 'password': '12312,./,.', 'expected_error': "Sorry, that password isn't valid. Please include a letter."},
        {'username': 'incorrect_username', 'password': 'incorrect_password', 'expected_error': "Looks like either the email/username or password is wrong. Try again, reset your password or get help."},
        {'username': 'bad@@email.com', 'password': '', 'expected_error': "Sorry, that email doesn’t look right. Please check it's a proper email."},
        {'username': 'bad@email', 'password': '', 'expected_error': "Sorry, that email doesn’t look right. Please check it's a proper email."},
        # Add more scenarios as needed
    ]

    for scenario in scenarios:
        # Enter the username and password
        page.fill('#user-identifier-input', scenario['username'])
        page.fill('#password-input', scenario['password'])

        # Click the Sign in
        page.click('#submit-button')

        # Define the selectors for username, password, and general error messages
        username_error_selector = '#form-message-username'
        password_error_selector = '#form-message-password'
        general_error_selector = '.form-message--general'

        # Wait for one of the error messages to appear
        page.wait_for_selector(f"{username_error_selector}, {password_error_selector}, {general_error_selector}")

        # Verify the error message
        actual_error_message = ''
        username_error_element = page.query_selector(username_error_selector)
        password_error_element = page.query_selector(password_error_selector)
        general_error_element = page.query_selector(general_error_selector)

        if username_error_element:
            actual_error_message = username_error_element.inner_text()
        elif password_error_element:
            actual_error_message = password_error_element.inner_text()
        elif general_error_element:
            actual_error_message = general_error_element.inner_text()

        assert actual_error_message == scenario['expected_error'], f"Expected: {scenario['expected_error']} but got: {actual_error_message}"