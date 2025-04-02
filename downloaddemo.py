from playwright.sync_api import sync_playwright

def download_handle(download):
    location_file = "./files/test.doc"
    download.save_as(location_file)


with sync_playwright() as p:
    browser = p.chromium.launch_persistent_context(
        user_data_dir = "user_data",
        headless=False,
        executable_path = "/usr/bin/brave-browser"
    )
    page = browser.new_page()
    page.goto("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
    page.on('download', download_handle)
    page.wait_for_selector('//a[@href="https://file-examples.com/wp-content/storage/2017/02/file-sample_100kB.doc"]').click()
    page.wait_for_timeout(3000)
