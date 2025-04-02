from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    try:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('https://demo.automationtesting.in/Selectable.html')

        # store multiple elements using list
        page.query_selector_all('d//[werf]').click()          # error handling
        elements = page.query_selector_all('a')
        print(len(elements))
        # for i in elements:
        #     print(i.text_content())
        # page.wait_for_timeout(2000)


        # store multiple href attributes
        for i in elements:
            print(i.text_content())
            #print(i.get_attribute('href'))
        page.wait_for_timeout(2000)
    except Exception as e:
        print(str(e))
    finally:         # what all code inside the finally will be run
        print('Execute')



