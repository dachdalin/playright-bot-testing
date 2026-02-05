from youtube import NoCostBot
import os

if __name__ == "__main__":
    # Use a generic keyword and channel that is likely to appear, or just test the navigation
    # For testing, we might want to check if it simply runs without crashing first.
    # The original script uses "Meow AI" and some keywords. Let's stick to that for now to reproduce the environment.
    bot = NoCostBot("entertaining content,funny video clips", "Meow AI")
    
    print("Starting single-run test...")
    bot.run_organic_session()
    print("Test finished.")
