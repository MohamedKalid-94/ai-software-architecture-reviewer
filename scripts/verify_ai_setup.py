import importlib

packages = [
    "langchain",
    "langgraph",
    "langsmith",
    "langchain_openai",
    "langchain_google_genai",
]

print("=" * 60)
print("AI Framework Verification")
print("=" * 60)

for package in packages:

    try:
        importlib.import_module(package)
        print(f"✅ {package}")

    except Exception as ex:
        print(f"❌ {package} -> {ex}")

print("=" * 60)