import time
import random
import os
from playwright.sync_api import sync_playwright
import playwright_stealth # Import the whole module

class NoCostBot:
    def __init__(self, keyword, channel, channel_url):
        self.keyword = keyword
        self.channel = channel
        self.channel_url = channel_url
        self.user_data_dir = os.path.abspath("chrome_profile")

    def run_organic_session(self):
        with sync_playwright() as p:
            # Persistent context saves cookies to look more human
            context = p.chromium.launch_persistent_context(
                self.user_data_dir,
                headless=True,
                args=["--disable-blink-features=AutomationControlled"],
                viewport={'width': 320, 'height': 640}
            )
            
            page = context.pages[0]
            
            # Application of stealth
            from playwright_stealth import Stealth
            stealth = Stealth()
            stealth.apply_stealth_sync(page)

            try:
                print(f"[{time.strftime('%H:%M:%S')}] Navigating to Google...")
                page.goto("https://www.google.com", wait_until="domcontentloaded")
                
                # Human-like typing
                search_box = page.get_by_role("combobox")
                search_box.click()
                for char in self.keyword:
                    page.keyboard.type(char, delay=random.randint(100, 250))
                page.keyboard.press("Enter")
                
                page.wait_for_load_state("networkidle")
                time.sleep(5)
                
                # Look for your channel name
                print(f"[*] Searching results for: {self.channel}")
                target = page.get_by_text(self.channel).first
                
                if target.is_visible():
                    target.click()
                    print("[+] Video Found! Watching...")
                    
                    # Capture proof
                    page.screenshot(path="youtube_proof.png")
                    
                    # Watch for a random amount of time
                    time.sleep(random.randint(60, 120))
                else:
                    print("[-] Video not found in the first results. Trying Direct Link...")
                    page.goto(self.channel_url, wait_until="domcontentloaded")
                    print("[+] Direct navigation successful! Watching...")
                    
                    page.screenshot(path="youtube_direct_proof.png")
                    time.sleep(random.randint(60, 120))

            except Exception as e:
                print(f"[-] Session Error: {e}")
            finally:
                context.close()

if __name__ == "__main__":
    # Ensure these match exactly what shows up in Google Search
    bot = NoCostBot(
        "entertaining content,funny video clips,entertaining content,lifestyle vlog,entertainment channel,viral content ideas", 
        "Meow AI",
        "https://www.youtube.com/@meowai-u9y/shorts"
    )
    
    while True:
        bot.run_organic_session()
        # Sleep 30-60 mins to protect your local IP
        delay = random.randint(1800, 3600)
        print(f"[*] Cycle finished. Sleeping {delay//60} mins to avoid IP ban...")
        time.sleep(delay)