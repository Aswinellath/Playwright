from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.google.com/")
    print(page.title())
    print('chrome successfully Launched')
    page.wait_for_timeout(3000)
   # browser.close()