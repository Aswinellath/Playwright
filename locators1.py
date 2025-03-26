from playwright.sync_api import sync_playwright

with sync_playwright() as play:
    browser = play.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://opensource-demo.orangehrmlive.com/')

    #using id
    # emailtxtbox = page.wait_for_selector('#email')
    # emailtxtbox.type('test@gmail.com')
    # page.wait_for_timeout(3000)
    # buttonlogin = page.wait_for_selector('#enterimg')
    # buttonlogin.click()
    # page.wait_for_timeout(3000)

    username = page.wait_for_selector('input[name="username"]')
    username.type('Admin')
    page.wait_for_timeout(3000)
    password = page.wait_for_selector('input[name="password"]')
    password.type('admin123')
    page.wait_for_timeout(3000)
    loginbutton = page.wait_for_selector('button[type="submit"]')
    loginbutton.click()
    page.wait_for_timeout(3000)
    print('code executed successfully')


