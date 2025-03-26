from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

    #xpath- Relative xpath
    #using attribute - //tagname[@attributename = "value"]
    # username_element = page.wait_for_selector('//input[@name="username"]')
    # password_element = page.wait_for_selector('//input[@name="password"]')
    # button_element = page.wait_for_selector('//button[@type="submit"]')
    # username_element.type('Admin')
    # page.wait_for_timeout(3000)
    # password_element.type('admin123')
    # page.wait_for_timeout(3000)
    # button_element.click()
    # page.wait_for_timeout(3000)
    # text - //tagname[text()="text"]

    # page.wait_for_selector('//p[text()="Forgot your password? "').click()
    # page.wait_for_timeout(3000)

    page.wait_for_selector('//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p').click()
    page.wait_for_timeout(3000)
    








