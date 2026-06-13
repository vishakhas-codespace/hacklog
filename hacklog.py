import random 
from datetime import date 
def welcome():
    facts = [
        "AI can detect cyberattacks  60x faster than humans.",
        "95% OF Cybersecurity breaches are caused by human error.",
        "The first computer virus was created in 1983 by fred cohen.",
        "By 2026, cybercrime costs the world over $10.5 trillion annually.",
        "AI is now being used to generate phishing emails that fool experts."
    ]

    print("╔══════════════════════════════════════╗")
    print("║   🔐 HACKLOG — Your Cyber Journal    ║")
    print("║   Built by a hacker in the making.  ║")
    print("╚══════════════════════════════════════╝")
    print()
    print(f"📡 Did you know?")
    print(f"   {random.choice(facts)}")
    print()

welcome()

def main_menu():
    print("What would you like to do today?")
    print()
    print("  [1] 📝 Log today's learning")
    print("  [2] 📖 View my journey")
    print("  [3] 🎯 Take a quick quiz")
    print("  [4] ⚡ Get today's challenge")
    print("  [5] 👋 Exit")
    print()
    choice = input("Your choice → ")
    return choice
welcome()
main_menu()

def log_learning():
    print()
    print("📝 What did you learn today, hacker?")
    entry = input("→ ")
    today = str(date.today())
    
    with open("hacklog.txt", "a") as f:
        f.write(f"[{today}] {entry}\n")
    
    print()
    print("✅ Logged! Every entry makes you stronger. 🔥")
    print()

def view_journey():
    print()
    try:
        with open("hacklog.txt", "r") as f:
            entries = f.readlines()
        if entries:
            print(f" Your journey so far — {len(entries)} entries:")
            print()
            for entry in entries:
                print(f"  {entry.strip()}")
        else:
            print("No entries yet. Start logging! ")
    except FileNotFoundError:
        print("No entries yet. Start logging! ")
    print()

    # after ALL def functions are done

welcome()
choice = main_menu()

if choice == "1":
    log_learning()
elif choice == "2":
    view_journey()
elif choice == "5":
    print()
    print("👋 Stay curious, stay dangerous. See you tomorrow!")