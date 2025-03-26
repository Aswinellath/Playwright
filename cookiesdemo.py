from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Gives all the cookies
    page.goto('https://www.redbus.in/')
    page.wait_for_timeout(3000)
    my_cookies = page.context.cookies()
    print(my_cookies)

    # clearing all the cookies
    page.context.cookies()

    new_cookie = {
        'name' : 'Aswin',
        'UDID' : '45261542y54545254t1222e'
    }

    # To pass the new cookies to the page
    # page.context.add_cookies([new_cookie])

    #Taking screenshot
    page.screenshot(path='test.png',full_page=True)