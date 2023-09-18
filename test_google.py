from selene.support.shared import browser
from selene import be, have

text = 'kdhcbkedfkefblhgleirhucsnhgkinhk'
text_assert = ('Результатов: примерно 0')

def test_google(open_link):
    browser.element('[name="q"]').should(be.blank).type(text).press_enter()
    # browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))
    browser.element('//*[@id="result-stats"]').should(have.text('Результатов: примерно 0'))
