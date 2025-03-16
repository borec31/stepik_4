import pytest

def pytest_configure(config):
    config.addinivalue_line("markers", "need_review: mark tests that need peer review")

@pytest.fixture(scope="session")
def browser():
    from selenium import webdriver
    driver = webdriver.Chrome()  # Предполагается, что ChromeDriver установлен
    yield driver
    driver.quit()
