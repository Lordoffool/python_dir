import random
import time

def print_slow(text, speed=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(speed)
    print()

def print_title():
    title = """
    ╔═══════════════════════════════════════╗
    ║   🎮 CRAZY FUN GAME ARENA 🎮          ║
    ║   Adventure Quest & Puzzle Madness    ║
    ╚═══════════════════════════════════════╝
    """
    print_slow(title, 0.02)

def riddle_game():
    riddles = [
        {
            "question": "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?",
            "answer": "echo",
            "hint": "Think of sound..."
        },
        {
            "question": "The more you take, the more you leave behind. What am I?",
            "answer": "footsteps",
            "hint": "Think of walking..."
        },
        {
            "question": "I have cities, but no houses. I have mountains, but no trees. What am I?",
            "answer": "map",
            "hint": "Think of geography..."
        }
    ]
    
    riddle = random.choice(riddles)
    print("\n" + "="*50)
    print_slow("🧩 RIDDLE TIME! 🧩", 0.03)
    print("="*50)
    print_slow(f"\n{riddle['question']}\n", 0.02)
    
    attempts = 3
    while attempts > 0:
        user_answer = input("Your answer: ").lower().strip()
        
        if user_answer == riddle['answer']:
            print_slow("\n🎉 CORRECT! You're a genius! 🎉\n", 0.03)
            return 10
        else:
            attempts -= 1
            if attempts > 0:
                print_slow(f"❌ Wrong! Hint: {riddle['hint']} ({attempts} attempts left)\n", 0.02)
            else:
                print_slow(f"\n😢 Game Over! The answer was: {riddle['answer']}\n", 0.02)
    return 0

def number_guessing_game():
    print("\n" + "="*50)
    print_slow("🎲 NUMBER GUESSING GAME 🎲", 0.03)
    print("="*50)
    
    secret = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    
    print_slow(f"\nI'm thinking of a number between 1 and 100...\n", 0.02)
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"Guess #{attempts + 1} ({max_attempts - attempts} left): "))
            attempts += 1
            
            if guess == secret:
                print_slow(f"\n🎯 BINGO! You found it in {attempts} attempts!\n", 0.03)
                return 20 - attempts
            elif guess < secret:
                print_slow("📈 Too low! Try higher...\n", 0.02)
            else:
                print_slow("📉 Too high! Try lower...\n", 0.02)
        except ValueError:
            print_slow("⚠️ Please enter a valid number!\n", 0.02)
    
    print_slow(f"\n😢 Game Over! The number was {secret}\n", 0.02)
    return 0

def memory_game():
    print("\n" + "="*50)
    print_slow("🧠 MEMORY CHALLENGE 🧠", 0.03)
    print("="*50)
    
    sequence = []
    player_sequence = []
    level = 1
    
    while True:
        sequence.append(random.randint(1, 4))
        player_sequence = []
        
        print_slow(f"\n⭐ Level {level}! Remember this sequence:\n", 0.02)
        for num in sequence:
            print(f"  {'🔴' if num == 1 else '🟡' if num == 2 else '🟢' if num == 3 else '🔵'}", end="")
            time.sleep(0.5)
        print("\n")
        
        for i in range(len(sequence)):
            try:
                user = int(input(f"Enter number {i+1}/{len(sequence)} (1-4): "))
                if user not in [1, 2, 3, 4]:
                    print_slow("⚠️ Enter 1, 2, 3, or 4!\n", 0.02)
                    return level * 5
                
                player_sequence.append(user)
                
                if player_sequence[-1] != sequence[-1]:
                    print_slow(f"\n❌ Wrong! You got to level {level}\n", 0.02)
                    return level * 5
            except ValueError:
                print_slow("⚠️ Please enter a valid number!\n", 0.02)
                return level * 5
        
        level += 1
        if level > 5:
            print_slow(f"\n🏆 INCREDIBLE! You beat all 5 levels!\n", 0.03)
            return 100

def adventure_game():
    print("\n" + "="*50)
    print_slow("⚔️ DUNGEON ADVENTURE ⚔️", 0.03)
    print("="*50)
    
    print_slow("\nYou enter a mysterious dungeon...\n", 0.02)
    time.sleep(1)
    
    hp = 100
    gold = 0
    choices = 0
    
    events = [
        {
            "text": "A wild DRAGON appears! 🐉",
            "options": ["Fight!", "Run!"],
            "outcomes": ["You slay the dragon! +50 gold 🪙", "You run away safely!"]
        },
        {
            "text": "You find a treasure chest! 💎",
            "options": ["Open it!", "Leave it"],
            "outcomes": ["You found 100 gold! 🪙", "You found a map instead!"]
        },
        {
            "text": "A mysterious wizard blocks your path! 🧙",
            "options": ["Challenge him!", "Negotiate"],
            "outcomes": ["Epic battle! You win! +75 gold 🪙", "He gives you a potion!"]
        }
    ]
    
    for event in events:
        print_slow(f"\n{event['text']}\n", 0.02)
        for i, option in enumerate(event['options'], 1):
            print(f"  {i}. {option}")
        
        try:
            choice = int(input("\nYour choice (1-2): ")) - 1
            if 0 <= choice < len(event['outcomes']):
                print_slow(f"\n✨ {event['outcomes'][choice]}\n", 0.02)
                choices += 1
            else:
                print_slow("⚠️ Invalid choice!\n", 0.02)
        except ValueError:
            print_slow("⚠️ Please enter a valid number!\n", 0.02)
    
    return choices * 25

def main_menu():
    print_title()
    
    total_score = 0
    
    while True:
        print("\n" + "="*50)
        print("🎮 CHOOSE YOUR ADVENTURE:")
        print("="*50)
        print("1. 🧩 Riddle Challenge")
        print("2. 🎲 Number Guessing Game")
        print("3. 🧠 Memory Challenge")
        print("4. ⚔️ Dungeon Adventure")
        print("5. 📊 View Score")
        print("6. 🚪 Exit")
        print("="*50)
        
        try:
            choice = input("\nEnter your choice (1-6): ").strip()
            
            if choice == "1":
                score = riddle_game()
                total_score += score
            elif choice == "2":
                score = number_guessing_game()
                total_score += score
            elif choice == "3":
                score = memory_game()
                total_score += score
            elif choice == "4":
                score = adventure_game()
                total_score += score
            elif choice == "5":
                print_slow(f"\n🏆 YOUR TOTAL SCORE: {total_score} points! 🏆\n", 0.03)
            elif choice == "6":
                print_slow(f"\n👋 Thanks for playing! Final Score: {total_score} 🎉\n", 0.03)
                break
            else:
                print_slow("⚠️ Invalid choice! Try again.\n", 0.02)
        except KeyboardInterrupt:
            print_slow("\n\n👋 Game interrupted! Final Score: " + str(total_score) + "\n", 0.02)
            break

if __name__ == "__main__":
    main_menu()
