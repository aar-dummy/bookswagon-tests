# Bookswagon E2E Test Suite

Selenium + Python E2E automation for [bookswagon.com](https://www.bookswagon.com).

## Project Structure

```
bookswagon_tests/
├── config.py               # URLs, credentials, timeouts
├── conftest.py             # pytest fixtures (driver, logged_in_driver)
├── pages/                  # Page Object Models
│   ├── base_page.py
│   ├── home_page.py
│   ├── login_page.py
│   ├── signup_page.py
│   ├── search_results_page.py
│   ├── product_detail_page.py
│   ├── cart_page.py
│   ├── wishlist_page.py
│   ├── category_page.py
│   ├── account_page.py
│   └── checkout_page.py
└── tests/
    ├── test_homepage.py    # Homepage load, nav, search
    ├── test_auth.py        # Login / Signup
    ├── test_search.py      # Search functionality
    ├── test_product.py     # Product detail page
    ├── test_cart.py        # Cart add/remove/checkout
    ├── test_wishlist.py    # Wishlist add/remove
    ├── test_navigation.py  # Category navigation
    ├── test_account.py     # Account pages
    └── test_checkout.py    # Checkout flow
```

## Setup

```bash
pip install -r bookswagon_tests/requirements.txt
```

For automatic ChromeDriver management, install `webdriver-manager` and update `conftest.py`:

```python
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opts)
```

## Configuration

Edit `bookswagon_tests/config.py`:

| Setting | Description |
|---|---|
| `TEST_EMAIL` | Valid account email for auth tests |
| `TEST_PASSWORD` | Account password |
| `BROWSER` | `"chrome"` or `"firefox"` |
| `HEADLESS` | `True` for CI/headless runs |

## Running Tests

```bash
# All tests
pytest

# Specific module
pytest bookswagon_tests/tests/test_search.py

# With HTML report
pytest --html=report.html

# Skip tests requiring login
pytest -k "not logged_in"
```

## Test Coverage

| Area | Tests |
|---|---|
| Homepage | Logo, nav, search box, title |
| Authentication | Login valid/invalid, signup validation |
| Search | Results, no-results, click-through, edge cases |
| Product Page | Title, price, add-to-cart, breadcrumb |
| Cart | Add, remove, total, checkout button |
| Wishlist | Add, remove, login-required guard |
| Navigation | Category nav links, category page products |
| Account | Orders, addresses, password, logout |
| Checkout | Login guard, address/payment sections |

## Notes

- Tests requiring login use the `logged_in_driver` fixture — set real credentials in `config.py`.
- Checkout and payment tests stop before placing a real order.
