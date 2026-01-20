#!/usr/bin/env python3
"""
Capture to PKM inbox - fast, low friction
Process later during weekly review
"""

from datetime import datetime
from pathlib import Path

INBOX = Path.home() / "pkm" / "inbox"

def capture():
    print("\n" + "="*50)
    print("CAPTURE TO INBOX")
    print("="*50)
    
    what = input("\nWhat? (brief description): ").strip()
    source = input("Source (url/book/podcast/twitter): ").strip()
    thread = input("Thread (architecture/philosophy/art/systems/unsure): ").strip()
    energy = input("Energy (high/med/low): ").strip()
    
    # Create filename from timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    safe_what = what[:30].replace(" ", "_").replace("/", "-")
    filename = f"{timestamp}_{safe_what}.md"
    
    # Build entry
    entry = f"# {what}\n\n"
    entry += f"**Captured:** {datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
    entry += f"**Source:** {source}\n"
    entry += f"**Thread:** {thread}\n"
    entry += f"**Energy:** {energy}\n"
    entry += f"\n---\n\n"
    entry += f"## Notes\n\n"
    entry += f"(Add notes here during processing)\n"
    
    # Save to inbox
    filepath = INBOX / filename
    with open(filepath, "w") as f:
        f.write(entry)
    
    print(f"\n✓ Saved to: {filepath}\n")

if __name__ == "__main__":
    capture()
