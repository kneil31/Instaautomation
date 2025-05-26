from playwright.sync_api import sync_playwright
import time
import os


def get_latest_image(folder="to_upload"):
    images = [f for f in os.listdir(folder) if f.lower().endswith((".jpg", ".jpeg", ".png"))]
    images.sort(key=lambda f: os.path.getmtime(os.path.join(folder, f)))
    return os.path.join(folder, images[-1]) if images else None


def post_to_instagram(image_path, caption):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(storage_state="state.json")
        page = context.new_page()
        page.goto("https://www.instagram.com/")
        page.wait_for_selector("svg[aria-label='New post'], svg[aria-label='Create']")
        page.click("svg[aria-label='New post'], svg[aria-label='Create']")

        # Wait for the real file input inside the dialog
        file_input = page.locator("div[role='dialog'] input[type='file']")
        file_input.set_input_files(image_path)

        # Click through the Next buttons
        page.wait_for_selector("text=Next")
        page.click("text=Next")
        page.wait_for_selector("text=Next")
        page.click("text=Next")

        # Fill caption and share
        page.wait_for_selector("textarea")
        page.fill("textarea", caption)
        page.click("text=Share")
        time.sleep(5)
        browser.close()


if __name__ == "__main__":
    latest_image = get_latest_image()
    caption = "Automated post via Playwright"
    if latest_image:
        post_to_instagram(latest_image, caption)
    else:
        print("No image found in to_upload folder")
