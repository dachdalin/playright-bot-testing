# Playright Bot Testing

A collection of Playwright-based automation scripts for testing and bot detection evasion techniques.

## Project Overview

This project contains various Python scripts that demonstrate different approaches to web automation using Playwright, with a focus on:
- Bot detection evasion using stealth techniques
- Organic browsing simulation
- YouTube content interaction automation
- Click traffic generation

## Project Structure

```
playright-bot-testing/
├── youtube.py              # Main YouTube bot with stealth features
├── test_youtube.py         # Test script for YouTube bot
├── impres.py              # Click traffic generation bot
├── minimal_test.py        # Basic Playwright functionality test
├── inspect_stealth.py     # Stealth library inspection utility
├── chrome_profile/        # Persistent browser profile directory
├── output.log            # Application logs
├── traffic.log           # Traffic generation logs
└── youtube_direct_proof.png  # Screenshot proof of bot execution
```

## Files Description

### Core Scripts

#### `youtube.py`
The main YouTube automation bot (`NoCostBot` class) that:
- Searches for videos on Google using human-like typing
- Navigates to YouTube channels
- Watches videos for random durations (60-120 seconds)
- Uses persistent Chrome profiles for realistic behavior
- Implements stealth techniques to avoid bot detection
- Takes screenshots as proof of execution

**Key Features:**
- Human-like typing with random delays (100-250ms per character)
- Mobile viewport simulation (320x640)
- Persistent context with saved cookies
- Stealth mode using `playwright-stealth` library
- Fallback to direct channel URL if search fails

#### `impres.py`
Advanced traffic generation bot (`UltimateBot` class) that:
- Generates click traffic to target URLs
- Uses rotating user agents and personas
- Simulates different geolocations and timezones
- Creates and manages Chrome profiles
- Implements cooling-down periods between requests

**Key Features:**
- Multiple persona support (location, timezone, locale)
- User agent rotation
- Geolocation spoofing
- Random click positions
- Persistent storage state management

#### `test_youtube.py`
Test script for the YouTube bot that:
- Imports and runs a single session of `NoCostBot`
- Uses simplified parameters for testing
- Validates basic bot functionality

#### `minimal_test.py`
Basic Playwright test script that:
- Verifies Playwright installation
- Tests basic browser launch and navigation
- Navigates to example.com and prints the page title

#### `inspect_stealth.py`
Diagnostic utility that:
- Inspects the `playwright-stealth` library structure
- Validates stealth module imports
- Helps troubleshoot stealth implementation issues

## Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Setup

1. Clone the repository:
```bash
git clone https://github.com/dachdalin/playright-bot-testing.git
cd playright-bot-testing
```

2. Install required dependencies:
```bash
pip install playwright playwright-stealth
```

3. Install Playwright browsers:
```bash
playwright install chromium
```

## Usage

### Running the YouTube Bot

**Single Session:**
```bash
python test_youtube.py
```

**Continuous Mode:**
```bash
python youtube.py
```

The bot will:
1. Search for specified keywords on Google
2. Look for the target channel name in results
3. Watch videos for 60-120 seconds
4. Sleep for 30-60 minutes between cycles
5. Take screenshots as proof

**Configuration:**
Edit the `youtube.py` file to customize:
```python
bot = NoCostBot(
    "your,keywords,here",           # Search keywords
    "Your Channel Name",             # Target channel name
    "https://youtube.com/@channel"   # Fallback URL
)
```

### Running the Traffic Bot

```bash
python impres.py
```

**Configuration:**
Edit the `impres.py` file to set your target:
```python
dataset = {
    "url": "https://your-target-url.com",
    "search_query": "search terms",
    "target_text": "link text to find"
}
```

### Running Minimal Test

To verify Playwright installation:
```bash
python minimal_test.py
```

Expected output:
```
Starting minimal test
Playwright initialized
Browser launched
Page created
Example Domain
Finished
```

### Inspecting Stealth Library

```bash
python inspect_stealth.py
```

## Dependencies

- **playwright**: Browser automation library
- **playwright-stealth**: Stealth plugin to avoid bot detection

## Features

### Bot Detection Evasion
- Disabled automation flags (`--disable-blink-features=AutomationControlled`)
- Stealth mode using `playwright-stealth`
- Human-like typing with random delays
- Random wait times and sleep intervals
- Persistent browser profiles with saved cookies
- Mobile and desktop user agent rotation

### Realistic Behavior Simulation
- Random typing delays (100-250ms per character)
- Random watch durations (60-120 seconds)
- Cool-down periods between sessions (30-60 minutes)
- Random mouse click positions
- Network idle state waiting

### Traffic Generation
- Multiple persona support (IP, location, language)
- Geolocation spoofing
- Timezone rotation
- User agent rotation
- Persistent storage state management

## Notes

- The `chrome_profile/` directory stores persistent browser data to simulate returning users
- Screenshots are saved as proof of successful navigation
- Logs are written to `output.log` and `traffic.log`
- The bots use headless mode by default for server deployment
- IP rate limiting: Built-in delays prevent IP bans from excessive requests

## Warning

This project is for educational and testing purposes only. Always:
- Respect website terms of service
- Comply with applicable laws and regulations
- Use responsibly and ethically
- Be aware of rate limiting and anti-bot measures
- Don't use for spam or malicious purposes

## License

This project is provided as-is for educational purposes.

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.
