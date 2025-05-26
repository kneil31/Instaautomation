from playwright.sync_api import sync_playwright

def save_session():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()

        page = context.new_page()
        page.goto("https://www.instagram.com")
        input("👉 Log in manually and press ENTER when done...")

        context.storage_state(path="state_chromium.json")
        print("✅ Session saved to state_chromium.json")
        browser.close()

if __name__ == "__main__":
    save_session()
