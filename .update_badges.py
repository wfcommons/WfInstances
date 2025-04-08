import requests
import re
import sys

README_PATH = sys.argv[1] if len(sys.argv) > 1 else "README.md"

totals_url = "https://wfinstances.ics.hawaii.edu/usage/public/totals/"
ips_url = "https://wfinstances.ics.hawaii.edu/usage/public/ips/"

totals = requests.get(totals_url).json()["result"]
ips = requests.get(ips_url).json()["result"]

downloads = totals.get("downloads", 0)
visualizations = totals.get("visualizations", 0)
simulations = totals.get("simulations", 0)
ip_count = len(ips)

with open(README_PATH, "r", encoding="utf-8") as f:
    content = f.read()

def replace_badge(text, label, value, color):
    return re.sub(
        rf"{label}-\d+-{color}\.svg",
        f"{label}-{value}-{color}.svg",
        text
    )

content = replace_badge(content, "downloads", downloads, "blue")
content = replace_badge(content, "visualizations", visualizations, "orange")
content = replace_badge(content, "simulations", simulations, "success")
content = replace_badge(content, "users", ip_count, "lightgrey")

with open(README_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print("✅ README badges updated:")
print(f"  Downloads      → {downloads}")
print(f"  Visualizations → {visualizations}")
print(f"  Simulations    → {simulations}")
print(f"  IPs (users)    → {ip_count}")
