import os

BASE_URL = "https://www.bookswagon.com"

# Reads from environment variables (set in GitHub Secrets); falls back to local values
TEST_EMAIL = os.getenv("TEST_EMAIL", "aarconn23@gmail.com")
TEST_PASSWORD = os.getenv("TEST_PASSWORD", "Password@12")
TEST_FIRST_NAME = "Aar"
TEST_LAST_NAME = "R"

# Timeouts
IMPLICIT_WAIT = 10
EXPLICIT_WAIT = 15
PAGE_LOAD_TIMEOUT = 30

# Browser: "chrome" or "firefox"
BROWSER = "chrome"
HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"

# Test data
SEARCH_QUERY = "harry potter"
SEARCH_QUERY_NO_RESULTS = "xyzxyzxyz123notabook"
CATEGORY_URL = f"{BASE_URL}/fiction"
