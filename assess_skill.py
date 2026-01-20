#!/usr/bin/env python3
"""
Skill Mastery Assessment Tool
Based on 4-level mastery rubric
"""

def assess_skill():
    print("\n" + "="*60)
    print("SKILL MASTERY ASSESSMENT")
    print("="*60)
    
    skill = input("\nWhat skill are you assessing? ")
    
    print(f"\nAssessing: {skill}")
    print("-"*60)
    
    # Level checks
    questions = [
        ("Can you do it without looking up instructions?", "L1: Execution"),
        ("Can you adapt it when context changes?", "L2: Transfer"),
        ("Can you name at least one failure mode?", "L2: Transfer"),
        ("Can you spot mistakes when others do it wrong?", "L3: Evaluation"),
        ("Can you teach it to someone else?", "L3: Evaluation")
    ]
    
    yes_count = 0
    for q, level in questions:
        answer = input(f"\n{q} (y/n): ").lower()
        if answer == 'y':
            yes_count += 1
    
    # Determine level
    if yes_count == 0:
        level = 0
        status = "Exposure"
        recommendation = "Practice with guided instructions"
    elif yes_count <= 1:
        level = 1
        status = "Execution"
        recommendation = "Try it in a different context"
    elif yes_count <= 3:
        level = 2
        status = "Transfer (MASTERED)"
        recommendation = "Ready to use independently"
    else:
        level = 3
        status = "Evaluation (TEACHING READY)"
        recommendation = "Can teach or design evals for this"
    
    print("\n" + "="*60)
    print(f"RESULT: Level {level} - {status}")
    print("="*60)
    print(f"Recommendation: {recommendation}")
    print("="*60 + "\n")
    
    # Log it
    with open("/Users/zeer0wan/skill_assessments.log", "a") as f:
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        f.write(f"[{timestamp}] {skill}: Level {level} ({status})\n")
    
    print(f"✓ Assessment logged to ~/skill_assessments.log\n")

if __name__ == "__main__":
    assess_skill()
