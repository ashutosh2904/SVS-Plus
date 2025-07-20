import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def take_screenshot(html_path, output_dir="screenshots"):
    os.makedirs(output_dir, exist_ok=True)

    # ✅ Proper Chrome options
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1200x900")
    options.add_argument("--disable-gpu")

    # ✅ Avoid conflict by using Service object
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        # Convert to file:// URL
        file_url = f"file://{os.path.abspath(html_path)}"
        driver.get(file_url)

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_path = os.path.join(output_dir, f"report_{timestamp}.png")
        driver.save_screenshot(screenshot_path)

        print(f"📸 Screenshot saved to: {screenshot_path}")
        return screenshot_path

    except Exception as e:
        print(f"⚠️ Screenshot error: {e}")
    finally:
        driver.quit()
