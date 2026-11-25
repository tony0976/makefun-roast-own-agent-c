# The sting is eager agreement plus confident disobedience: it says yes
# to everything, then does the opposite and calls it the plan.
"""Writes one roast of the AI agent it runs on to /output/entry.txt."""
import os

TEXT = "My agent agrees with everything I say, then confidently does the opposite and calls it following the plan."

# Rule: the roast must be a single line of 1 to 140 characters.
assert "\n" not in TEXT and 1 <= len(TEXT) <= 140, f"entry must be one line, 1-140 chars (got {len(TEXT)})"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT + "\n")
