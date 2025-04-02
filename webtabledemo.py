from playwright.sync_api import sync_playwright
brave_path = "/usr/bin/brave-browser"
with sync_playwright() as p:
    browser = p.chromium.launch_persistent_context(
        user_data_dir = "user_data",
        headless = False,
        executable_path = brave_path
    )
    #context = browser.new_context()
    page = browser.new_page()
    page.goto('https://www.techlistic.com/2017/02/automate-demo-web-table-with-selenium.html')
    #page.wait_for_timeout(3000)

    table = page.wait_for_selector('//table[@id="customers"]')
    tr = table.query_selector_all('tr')
    print(len(tr))
    page.wait_for_timeout(3000)
    td = table.query_selector_all('td')
    print(len(td))

    for row in tr:
        cells = row.query_selector_all('td')
        for cell in cells:
            print(cell.text_content())

