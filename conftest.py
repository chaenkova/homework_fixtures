import pytest
from selene import browser

@pytest.fixture(scope="session",autouse=True)
def browser_settings():
    print("Браузер!")
    browser.config.window_height = 1080
    browser.config.window_width = 1920

    yield
    browser.quit()
    print("Закрываем браузер!")

@pytest.fixture
def open_google():
    return 'https://google.com'
@pytest.fixture
def open_yandex():
    return 'https://ya.ru'
