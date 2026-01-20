#!/usr/bin/env python3
"""
Quick INBOX triage - shows what needs attention
"""

from pathlib import Path
from datetime import datetime

inbox = Path.home() / "Desktop" / "00_INBOX"

print("\n" + "="*50)
print("INBOX TRIAGE")
print("="*50 + "\n")

items = list(inbox.iterdir())

if not items:
    print("✓ INBOX is empty!\n")
else:
    print(f"You have {len(items)} items:\n")
    
    for item in sorted(items):
        if item.name.startswith('.'):
            continue
            
        # Get how old the file is
        age_days = (datetime.now().timestamp() - item.stat().st_mtime) / 86400
        
        if item.is_dir():
            count = len(list(item.iterdir()))
            print(f"📁 {item.name}/ ({count} items, {age_days:.0f} days old)")
        else:
            size_kb = item.stat().st_size / 1024
            print(f"📄 {item.name} ({size_kb:.1f}KB, {age_days:.0f} days old)")
    
    print("\n" + "="*50)
    print("Items over 7 days old should be processed or archived.")
    print("="*50 + "\n")
