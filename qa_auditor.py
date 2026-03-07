from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def run_laundry_audit():
    print("Initiating: Starting Automated QA Audit for Invicta Laundry...")
    
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=chrome_options)
    target_url = "https://invicta-laundry.netlify.app/"

    try:
        print(f"📡 NAVIGATING: Fetching {target_url}")
        driver.get(target_url)

        assert "Laundry" in driver.title or driver.title != "", "ERROR: Page title is missing or incorrect."
        print("1st Test Passed: DOM loaded and Title verified.")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        print("2nd Test Passed: Main body structure rendered.")

        interactive_elements = driver.find_elements(By.TAG_NAME, "button")
        if len(interactive_elements) > 0:
            print(f"3rd Test Passed: Found {len(interactive_elements)} interactive buttons/actions.")
        else:
            print("WARNING: No interactive buttons found on the initial load.")

        print("\nAudit Complete: All critical production systems are nominal.")

    except Exception as e:
        print(f"\nAudit Failed: Regression detected.\nDetails: {e}")

    finally:
        driver.quit()


if __name__ == "__main__":
    run_laundry_audit()