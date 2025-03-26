from playwright.sync_api import sync_playwright
text_alert = []


def handle_dialog(dialog):
    message = dialog.type
    text_alert.append(message)
    dialog.accept()


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://demo.automationtesting.in/Alerts.html')
    AlertOKbutton = page.wait_for_selector('//a[@href="#Textbox"]')
    AlertOKbutton.click()
    page.wait_for_timeout(3000)
    # page.on("dialog",lambda dialog : print(dialog.message))
    # page.on("dialog",lambda dialog : print(dialog.accept()))
    page.on("dialog",handle_dialog)
    Confirmbutton = page.wait_for_selector('//div[@id="Textbox"]/button')
    Confirmbutton.click()
    page.wait_for_timeout(3000)
    print(text_alert[0])






