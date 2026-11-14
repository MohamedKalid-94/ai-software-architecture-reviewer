import requests

BASE_URL = "http://localhost:8000"

def check_backend_health():
    response = requests.get(
        f"{BASE_URL}/api/v1/health",
        timeout=10,
    )
    response.raise_for_status()
    return response.json()