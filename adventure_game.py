def start_game():
    print("Welcome to the Adventure Game!")
    print("You are standing in a dark forest. There are two paths ahead.")
    print("1. Take the left path.")
    print("2. Take the right path.")

    global health
    health = 100

    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        left_path()
    elif choice == '2':
        right_path()
    else:
        print("Invalid choice. Please try again.")
        start_game()

def left_path():
    print("You took the left path.")
    print("You encounter a friendly goblin.")
    print("1. Talk to the goblin.")
    print("2. Run away.")

    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        print("The goblin gives you a magic sword!")
    elif choice == '2':
        print("You escape, but find nothing.")
    else:
        print("Invalid choice. Please try again.")
        left_path()

def right_path():
    print("You took the right path.")
    print("You find a locked treasure chest.")
    print("1. Try to open the chest.")
    print("2. Leave the chest alone.")

    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        print("The chest is trapped! You lose some health.")
        health -= 20
        print(f"Your health is now {health}.")
        if health <= 0:
            print("Game Over! You ran out of health.")
    elif choice == '2':
        print("You decide to leave it and continue your journey.")
    else:
        print("Invalid choice. Please try again.")
        right_path()

start_game()
