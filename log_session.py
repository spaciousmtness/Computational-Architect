#!/usr/bin/env python3
"""
Session Logger - Track what you accomplish each session
"""

from datetime import datetime
from pathlib import Path

log_file = Path.home() / "work_log.txt"

# Get input
print("\n" + "="*50)
print("SESSION LOGGER")
print("="*50)
what_done = input("\nWhat did you accomplish this session?\n> ")

# Write to log
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
with open(log_file, "a") as f:
    f.write(f"[{timestamp}] {what_done}\n")

print("\n✓ Logged!")

# Show recent entries
if log_file.exists():
    with open(log_file, "r") as f:
        lines = f.readlines()
        recent = lines[-5:]
    
    print("\nYour last 5 sessions:")
    print("-" * 50)
    for line in recent:
        print(line.strip())
    print("="*50 + "\n")
