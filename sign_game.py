import random
import string

signs = ['rock', 'paper', 'scissor']

print("\n------WELCOME to the ROCK-PAPER-SCISSOR game------")

def show_menu():
    print("\nMenu:", "1 - View signs", "2 - New game", "3 - Load Saved game", "4 - Exit game", sep="\n")

def computer_choice():
    return random.choice(signs)

def view_sign():
    if not signs:
        print("No signs available!")
    else:
        print("\nAvailable signs:")
        for index, sign in enumerate(signs):
            print(f"{index+1}. {sign}")

def new_game():
    u_score, c_score = 0, 0

    print("\n--- Starting New Game ---")
    print("Type 'exit' to go back to menu.\n")
    while True:
        user_choice = input("Your choice (rock/paper/scissor): ").lower().strip()
        if user_choice == "exit":
            print("Returning to menu...\n")
            break
        if user_choice not in signs:
            print("Invalid choice! Please select from rock, paper, or scissor.")
            continue

        print("\nGenerating computer's choice...")
        com_choice = computer_choice()
        print(f"Computer's choice: {com_choice}")

        if user_choice == com_choice:
            print("\nIt's a draw!")
        elif (user_choice == "rock" and com_choice == "scissor") or \
                (user_choice == "paper" and com_choice == "rock") or \
                (user_choice == "scissor" and com_choice == "paper"):
            print("\nYou win this round!")
            u_score += 1
        else:
            print("\nComputer wins this round!")
            c_score += 1

        print(f"Score => You: {u_score} | Computer: {c_score}\n")


def exit_game():
    print("\nExiting game...")
    print("\nThank you for playing!")
    global running
    running = False

menu = {
    "1": view_sign,
    "2": new_game,
    "4": exit_game
}


running = True
while running:
    show_menu()
    choice = input("\nEnter your choice: ").strip()
    action = menu.get(choice)

    if action:
        action()
    else:
        print("Invalid choice, please try again!")