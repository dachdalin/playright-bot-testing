import playwright_stealth
import inspect

print(f"playwright_stealth type: {type(playwright_stealth)}")
print(f"playwright_stealth dir: {dir(playwright_stealth)}")

if hasattr(playwright_stealth, 'stealth'):
    print(f"playwright_stealth.stealth type: {type(playwright_stealth.stealth)}")
    print(f"playwright_stealth.stealth dir: {dir(playwright_stealth.stealth)}")
else:
    print("playwright_stealth has no 'stealth' attribute")

try:
    from playwright_stealth import stealth
    print(f"imported stealth type: {type(stealth)}")
except ImportError as e:
    print(f"ImportError: {e}")
