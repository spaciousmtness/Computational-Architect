#!/usr/bin/env python3
"""
Daily Ritual - Morning Computing Environment Check
Run this every morning to keep your digital life organized
"""

import os
from datetime import datetime
from pathlib import Path

def show_header():
    """Display welcome message"""
    today = datetime.now().strftime("%A, %B %d, %Y")
    print("\n" + "="*60)
    print(f"DAILY RITUAL - {today}")
    print("="*60 + "\n")

def check_inbox():
    """Show what's waiting in your inbox"""
    inbox_path = Path.home() / "Desktop" / "00_INBOX"
    
    print("INBOX STATUS:")
    print("-" * 60)
    
    if not inbox_path.exists():
        print("ERROR: INBOX folder not found!")
        return
    
    items = list(inbox_path.iterdir())
    
    if not items:
        print("Inbox is empty - nice work!\n")
        return
    
    print(f"You have {len(items)} item(s) waiting:\n")
    
    for item in sorted(items):
        if item.name.startswith('.'):
            continue  # Skip hidden files
        
        if item.is_dir():
            file_count = len(list(item.iterdir()))
            print(f"  [FOLDER] {item.name}/ ({file_count} items inside)")
        else:
            # Show file size
            size_mb = item.stat().st_size / (1024 * 1024)
            print(f"  [FILE] {item.name} ({size_mb:.2f} MB)")
    
    print()

def show_naming_reminder():
    """Remind about file naming standard"""
    print("FILE NAMING STANDARD:")
    print("-" * 60)
    print("Format: YYYY-MM-DD_project-name_description.ext")
    print("Example: 2026-01-14_daylight-ops_budget-report.xlsx")
    print()

def check_desktop():
    """Make sure Desktop stays clean"""
    desktop_path = Path.home() / "Desktop"
    
    print("DESKTOP CHECK:")
    print("-" * 60)
    
    items = [item for item in desktop_path.iterdir() 
             if not item.name.startswith('.') 
             and item.name not in ['00_INBOX', '00_ARCHIVE_2025']]
    
    if not items:
        print("Desktop is clean!\n")
    else:
        print(f"WARNING: {len(items)} item(s) on Desktop that should be moved:\n")
        for item in items:
            print(f"  -> {item.name}")
        print("\nMove these to 00_INBOX or 00_ARCHIVE_2025\n")

def show_footer():
    """Display closing message"""
    print("="*60)
    print("Ready to build? Let's go.")
    print("="*60 + "\n")

def main():
    """Run the daily ritual"""
    show_header()
    check_inbox()
    show_naming_reminder()
    check_desktop()
    show_footer()

if __name__ == "__main__":
    main()
