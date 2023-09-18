import pytest
from selene.support.shared import browser
from selene import be, have


@pytest.fixture()
def open_link():
    browser.with_(window_height=1200, window_width=700).open('https://www.google.com/')
