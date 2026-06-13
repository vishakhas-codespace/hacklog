import random
from datetime import date

def welcome():
    facts = [
        "AI can detect cyberattacks 60x faster than humans.",
        "95% of cybersecurity breaches are caused by human error.",
        "The first computer virus was created in 1983 by Fred Cohen.",
        "By 2026, cybercrime costs the world over $10.5 trillion annually.",
        "AI is now being used to generate phishing emails that fool experts."
    ]
    print("╔══════════════════════════════════════╗")
    print("║   🔐 HACKLOG — Your Cyber Journal    ║")
    print("║   Built by a hacker in the making.  ║")
    print("╚══════════════════════════════════════╝")
    print()
    print("📡 Did you know?")
    print(f"   {random.choice(facts)}")
    print()

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
            print(f"📖 Your journey so far — {len(entries)} entries:")
            print()
            for entry in entries:
                print(f"  {entry.strip()}")
        else:
            print("No entries yet. Start logging! 💪")
    except FileNotFoundError:
        print("No entries yet. Start logging! 💪")
    print()

def quick_quiz():
    questions = [
        {"q": "What does VPN stand for?", "a": "virtual private network"},
        {"q": "What attack tricks users into revealing passwords?", "a": "phishing"},
        {"q": "What does 2FA stand for?", "a": "two factor authentication"},
        {"q": "Malicious software that encrypts files and demands payment?", "a": "ransomware"},
        {"q": "What does SQL injection attack?", "a": "database"}
    ]
    q = random.choice(questions)
    print()
    print("🎯 Quick Quiz!")
    print()
    print(f"❓ {q['q']}")
    answer = input("→ ").lower().strip()
    if answer == q['a']:
        print()
        print("✅ Correct! You're built different. 🔥")
    else:
        print()
        print(f"❌ Not quite! The answer was: {q['a']}")
        print("📖 Look it up and add it to your HackLog!")
    print()

def daily_challenge():
    challenges = [
        "Research what a man-in-the-middle attack is and write 3 lines about it.",
        "Find out what port 443 is used for.",
        "Look up what OSINT means and find one free OSINT tool.",
        "Research the difference between symmetric and asymmetric encryption.",
        "Find out what a zero-day vulnerability is.",
        "Look up what Wireshark is and what it's used for.",
        "Research what social engineering means in cybersecurity.",
        "Find out what a honeypot is in network security.",
        "Look up the OWASP Top 10 and write down the first 3.",
        "Research what penetration testing is."
    ]
    print()
    print("⚡ Today's Challenge:")
    print()
    print(f"  {random.choice(challenges)}")
    print()
    print("📝 Complete it and log what you learned!")
    print()

# --- run the app ---
welcome()
choice = main_menu()

if choice == "1":
    log_learning()
elif choice == "2":
    view_journey()
elif choice == "3":
    quick_quiz()
elif choice == "4":
    daily_challenge()
elif choice == "5":
    print()
    print("👋 Stay curious, stay dangerous. See you tomorrow!")