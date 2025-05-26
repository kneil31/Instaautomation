from playwright.sync_api import sync_playwright
import time, os

def post_to_instagram(image_path, caption_text):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(storage_state="state.json")
        page = context.new_page()
        page.goto("https://www.instagram.com/")

        # Wait for page and create button
        page.wait_for_selector("svg[aria-label='New post'], svg[aria-label='Create']")
        page.click("svg[aria-label='New post'], svg[aria-label='Create']")
        time.sleep(2)

        # Find and click file input field
        file_input = page.locator("input[type='file']")
        file_input.set_input_files(image_path)
        print("✅ Image uploaded")

        # Wait and click "Next"
        page.wait_for_selector("text=Next")
        page.click("text=Next")
        time.sleep(2)

        # Wait and click "Next" again (filter step)
        page.wait_for_selector("text=Next")
        page.click("text=Next")
        time.sleep(2)

        # Fill caption
        page.wait_for_selector("textarea")
        page.fill("textarea", caption_text)
        time.sleep(2)

        # Share
        page.click("text=Share")
        print("🚀 Post shared!")
        time.sleep(5)

        browser.close()

if __name__ == "__main__":
    post_to_instagram("test_image.jpg", "This is an automated post using Playwright 📸")
