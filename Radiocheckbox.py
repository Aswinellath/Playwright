from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://demo.automationtesting.in/Register.html')
    page.wait_for_timeout(3000)
    #Radio Button
    radio_button = page.query_selector('//input[@value="Male"]')

    radio_button2 = page.query_selector('//input[@value="FeMale"]')
    #click and check
    radio_button.click()

    page.wait_for_timeout(3000)
    #radio_button2.check()
    page.wait_for_timeout(2000)
    if radio_button.is_checked():
        print('Male is checked')
    else:
        print('Female is checked')
    page.wait_for_timeout(3000)
    checkbox1 = page.query_selector('//input[@value="Cricket"]')
    checkbox2 = page.query_selector('//input[@value="Movies"]')
    checkbox3 = page.query_selector('//input[@value="Hockey"]')
    page.wait_for_timeout(2000)
    #checkbox1.click()
    page.wait_for_timeout(2000)
    checkbox2.click()
    page.wait_for_timeout(2000)
    checkbox3.click()
    page.wait_for_timeout(2000)
    if checkbox1.is_checked():
        print('Cricket is checked')
    else:
        print('Cricket is not checked')
    if checkbox2.is_checked():
        print('Movie is checked')
    else:
        print('Movie is not checked')
    if checkbox3.is_checked():
        print('Hockey is checked')
    else:
        print('Hockey is not checked')
    page.wait_for_timeout(4000)

