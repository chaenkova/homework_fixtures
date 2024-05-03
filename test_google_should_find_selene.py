from selene import browser, be, have

def test_google_find_selene(open_google):
    browser.open(open_google)
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_google_do_not_find_coffe(open_google):
    browser.open(open_google)
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.no.text('Coffe'))

def test_google_do_not_find_anything(open_google):
    browser.open(open_google)
    browser.element('[name="q"]').should(be.blank).type('-ygmhv hghbxdfghjkl;lkjuhygtfdsdfghjkl;lkjhgfdx').press_enter()
    browser.element('#result-stats').should(have.text('Результатов: примерно 0'))

def test_yandex_find_selene(open_yandex):
    browser.open(open_yandex)
    browser.element('#text').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('#search-result').should(have.text('yashaka/selene: User-oriented Web UI browser...'))

def test_yandex_do_not_find_coffe(open_yandex):
    browser.open(open_yandex)
    browser.element('#text').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('#search-result').should(have.no.text('Coffe'))
