from playwright.sync_api import Playwright, sync_playwright
brave_path = "/usr/bin/brave-browser"
with sync_playwright() as p:
    browser = p.chromium.launch_persistent_context(
        user_data_dir = "user_data",
        headless = False,
        executable_path = brave_path
    )
    page = browser.new_page()
    page.goto('https://demo.automationtesting.in/FileUpload.html')
    file_upload = './test.txt'
    upload_location = page.query_selector('//input[@id="input-4"]')

    # To upload the file

    upload_location.set_input_files(file_upload)
    page.wait_for_timeout(8000)
