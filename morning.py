#!/usr/bin/env python3
"""
Morning Routine - Complete environment check + recent work log
"""

import subprocess
from pathlib import Path
from datetime import datetime

def run_command(cmd):
    """Run a shell command and return output"""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout

def show_recent_logs():
    """Show last 3 work sessions"""
    log_file = Path.home() / "work_log.txt"
    
    if not log_file.exists():
        return
    
    with open(log_file, "r") as f:
        lines = f.readlines()
        recent = lines[-3:]
    
    print("\n" + "="*60)
    print("RECENT WORK SESSIONS")
    print("="*60)
    for line in recent:
        print(line.strip())
    print("="*60 + "\n")

if __name__ == "__main__":
    print("\n" + "🌅 " + "="*56)
    print(f"   GOOD MORNING - {datetime.now().strftime('%A, %B %d, %Y')}")
    print("="*60 + "\n")
    
    # Run ritual
    print(run_command("python3 ~/scripts/daily_ritual.py"))
    
    # Run triage
    print(run_command("python3 ~/scripts/inbox_check.py"))
    
    # Show recent work
    show_recent_logs()
    
    print("="*60)
    print("What will you build today?")
    print("="*60 + "\n")
