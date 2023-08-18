# UI Tests for https://www.bbc.co.uk/sport/football/scores-fixtures

This repository contains automated UI tests for https://www.bbc.co.uk/sport/football/scores-fixtures. The tests are written in Python and use pytest and Playwright to perform UI testing of the website.

---

## Getting Started
These instructions will provide guidance on setting up the test suite on your local machine.

### Prerequisites
- Python 3.9 or higher
- Playwright
- pytest

### Installation
1. Install virtualenv https://virtualenv.pypa.io/en/stable/installation.html
2. Navigate to the project directory after cloning the repo:
   > `cd ui-test/`
3. Install the required dependencies:
   > `pip install -r requirements.txt`
4. Install Playwright drivers:
   > `playwright install`

## Running the Tests
Run all tests with the following command:

> `pytest`

Run a specific test with:

>`pytest path/to/your/test.py`

## Test Scenarios
The test suite includes various scenarios. Here are some of the covered areas:
- Verifying UI elements and displaying the result
- Searching and navigating through different sections
- Negative user login scenarios

You can find the detailed test cases in the \`tests/\` directory.
