from playwright.sync_api import sync_playwright
import time, os

def get_latest_image(folder="to_upload"):
    image_files = [f for f in os.listdir(folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    if not image_files:
        raise FileNotFoundError("No image files found in folder.")

    image_files.sort(key=lambda x: os.path.getmtime(os.path.join(folder, x)))
    return os.path.join(folder, image_files[-1])

def post_to_instagram(image_path, caption_text):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(storage_state="state.json")
        page = context.new_page()
        page.goto("https://www.instagram.com/")
        time.sleep(5)

        page.click("svg[aria-label='New post'], svg[aria-label='Create']")
        time.sleep(3)

        # Simulate click into upload zone (manual file picker)
        page.mouse.click(300, 400)
        print("🛠️ Please select the file manually in the dialog.")
        input("✅ Press ENTER after upload is done...")

        page.click("text=Next")
        time.sleep(2)

        page.click("text=Next")
        time.sleep(2)

        page.fill("textarea", caption_text)
        time.sleep(2)

        page.click("text=Share")
        print("🚀 Post shared!")
        time.sleep(5)

        browser.close()

if __name__ == "__main__":
    latest_image = get_latest_image("to_upload")
    post_to_instagram(latest_image, "📸 Automatically posted image via Playwright!")
