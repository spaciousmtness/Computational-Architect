#!/usr/bin/env python3
"""Track videos, articles, links to consume"""

from datetime import datetime
from pathlib import Path

MEDIA_FILE = Path.home() / "notebooks" / "media_tracker.md"

def add_item():
    print("\n" + "="*50)
    print("ADD MEDIA TO TRACK")
    print("="*50)
    
    media_type = input("\nType (video/article/link/book): ").strip()
    title = input("Title: ").strip()
    url = input("URL (or 'none'): ").strip()
    why = input("Why save this?: ").strip()
    
    timestamp = datetime.now().strftime("%Y-%m-%d")
    
    entry = f"\n## [{timestamp}] {title}\n"
    entry += f"- Type: {media_type}\n"
    entry += f"- URL: {url}\n"
    entry += f"- Why: {why}\n"
    entry += f"- Status: TO CONSUME\n"
    
    with open(MEDIA_FILE, "a") as f:
        f.write(entry)
    
    print(f"\n✓ Added to {MEDIA_FILE}\n")

if __name__ == "__main__":
    add_item()
