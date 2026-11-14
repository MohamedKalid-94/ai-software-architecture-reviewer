from pathlib import Path

required = [
    "backend",
    "frontend",
    "agents",
    "graphs",
    "prompts",
    "datasets",
    "evaluations",
]

missing = []

for folder in required:
    if not Path(folder).exists():
        missing.append(folder)

if missing:
    print("Missing folders:")
    for item in missing:
        print("-", item)
else:
    print("Project structure verified.")