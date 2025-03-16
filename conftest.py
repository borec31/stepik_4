import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption(
        "--language",
        action="store",
        default="en",
        help="Choose language: en, es, fr, etc."
    )

def pytest_configure(config):
    config.addinivalue_line("markers", "need_review: mark tests that need peer review")

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("--language")
    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", {"intl.accept_languages": language})
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
