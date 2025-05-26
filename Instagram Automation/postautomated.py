from playwright.sync_api import sync_playwright
import os
import time

def get_latest_image(folder_path):
    images = [f for f in os.listdir(folder_path) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    images.sort(key=lambda f: os.path.getmtime(os.path.join(folder_path, f)))
    return os.path.join(folder_path, images[-1]) if images else None

def post_to_instagram(image_path, caption):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(storage_state="state_chromium.json")
        page = context.new_page()
        page.goto("https://www.instagram.com/")
        time.sleep(5)

        # STEP 1: Inject file input and upload image
        page.evaluate("""
        () => {
            const input = document.createElement('input');
            input.type = 'file';
            input.accept = 'image/*';
            input.id = 'upload-hack';
            input.style.position = 'fixed';
            input.style.top = '100px';
            input.style.left = '100px';
            input.style.zIndex = 9999;
            document.body.appendChild(input);
        }
        """)
        print("📂 Uploading image...")
        page.set_input_files("#upload-hack", image_path)
        time.sleep(3)

        # STEP 2: Click "Next" button 1
        print("⏭️ Clicking Next #1 (coordinates)...")
        page.mouse.click(800, 750)
        time.sleep(2)

        # STEP 3: Click "Next" button 2
        print("⏭️ Clicking Next #2 (coordinates)...")
        page.mouse.click(800, 750)
        time.sleep(2)

        # STEP 4: Type caption
        print("📝 Typing caption...")
        page.keyboard.type(caption)
        time.sleep(1)

        # STEP 5: Click Share
        print("📤 Clicking Share (coordinates)...")
        page.mouse.click(800, 950)
        print("✅ Post shared!")
        time.sleep(5)

        browser.close()

# MAIN RUN
folder = "to_upload"
image_path = get_latest_image(folder)
caption = "📸 Posted via visual automation with Playwright mouse clicks"
if image_path:
    post_to_instagram(image_path, caption)
else:
    print("❌ No image found.")
