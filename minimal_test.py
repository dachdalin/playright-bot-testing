from playwright.sync_api import sync_playwright

print("Starting minimal test")
with sync_playwright() as p:
    print("Playwright initialized")
    browser = p.chromium.launch(headless=True)
    print("Browser launched")
    page = browser.new_page()
    print("Page created")
    page.goto("https://example.com")
    print(page.title())
    browser.close()
print("Finished")
