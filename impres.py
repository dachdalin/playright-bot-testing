import time
import random
from playwright.sync_api import sync_playwright

class UltimateBot:
    def __init__(self, target_url, search_query, target_name):
        self.target_url = target_url
        self.search_query = search_query
        self.target_name = target_name
        # Define a list of "Personas" - IP + Location + Language
        # As an engineer, you can expand this list to hundreds of entries
        self.personas = [
            {
                "lat": 40.7128, "lng": -74.0060, 
                "tz": "America/New_York", "locale": "en-US"
            },
            {
                "lat": 51.5074, "lng": -0.1278, 
                "tz": "Europe/London", "locale": "en-GB"
            }
        ]
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        ]

    def run(self):
        with sync_playwright() as p:
            # Headless=True for background running on Ubuntu
            browser = p.chromium.launch(headless=True, args=["--disable-blink-features=AutomationControlled"])
            print(f"[*] Engine Started. Targeting: {self.target_name}")

            try:
                while True:
                    # 1. CHECK AND CREATE CHROME PROFILE IF NOT EXISTS
                    storage_state_path = "chrome_profile/Default/storage_state.json"
                    try:
                        with open(storage_state_path, "r") as f:
                            pass  # File exists, no action needed
                    except FileNotFoundError:
                        print("[!] Storage state file not found. Creating a new one.")
                        context = browser.new_context()
                        context.storage_state(path=storage_state_path)
                        context.close()

                    # 2. CREATE CHROME PROFILE
                    context = browser.new_context(
                        user_agent=random.choice(self.user_agents),
                        permissions=["geolocation"],
                        geolocation={"latitude": 40.7128, "longitude": -74.0060},
                        timezone_id="America/New_York",
                        locale="en-US",
                        viewport={'width': 1920, 'height': 1080},
                        storage_state=storage_state_path
                    )

                    page = context.new_page()

                    try:
                        print(f"[{time.strftime('%H:%M:%S')}] Using Chrome profile")

                        # 3. OPEN TARGET URL
                        print(f"[*] Navigating to target URL...")
                        page.goto(self.target_url, timeout=60000, wait_until="domcontentloaded")

                        print("[+] Page loaded. Clicking link...")
                        time.sleep(5)  # Wait 5 seconds before clicking

                        # Click a random spot in the center area
                        page.mouse.click(random.randint(400, 800), random.randint(300, 600))
                        print(f"[+] Link clicked. Closing profile...")

                    except Exception as e:
                        print(f"[-] Session Failed: {e}")

                    # 4. CLEANUP
                    context.close()
                    print("[*] Profile destroyed. Cooling down for 5s...")
                    time.sleep(5)

            except KeyboardInterrupt:
                print("\n[!] Loop terminated.")
            finally:
                browser.close()

if __name__ == "__main__":
    # Example Config
    dataset = {
        "url": "https://enoughprosperabsorbed.com/z0qij20izr?key=c7259c658d8691b654ecf23c43bf2917",
        "search_query": "site:enoughprosperabsorbed.com z0qij20izr", # Example search query to find the site
        "target_text": "enoughprosperabsorbed" # Text likely to appear in the Google result link
    }
    
    bot = UltimateBot(dataset["url"], dataset["search_query"], dataset["target_text"])
    bot.run()