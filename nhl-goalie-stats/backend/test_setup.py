print("=" * 50)
print("Python Setup Test")
print("=" * 50)

import sys
print(f"\nPython version: {sys.version}")
print(f"Python executable: {sys.executable}")

try:
    import flask
    print(f"\n✓ Flask installed: {flask.__version__}")
except ImportError:
    print("\n✗ Flask not installed")

try:
    import flask_cors
    print(f"✓ Flask-CORS installed: {flask_cors.__version__}")
except ImportError:
    print("✗ Flask-CORS not installed")

try:
    import requests
    print(f"✓ Requests installed: {requests.__version__}")
except ImportError:
    print("✗ Requests not installed")

print("\n" + "=" * 50)
print("🏒 Hello World from NHL Goalie App! 🥅")
print("=" * 50)