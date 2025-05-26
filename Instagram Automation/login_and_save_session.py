from playwright.sync_api import sync_playwright

def save_session_with_edge():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            executable_path="/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
            headless=False
        )

        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.instagram.com")

        print("👉 Please log in manually in Edge, then press Enter here...")
        input()

        context.storage_state(path="state.json")
        print("✅ Session saved to state.json")
        browser.close()

if __name__ == "__main__":
    save_session_with_edge()
