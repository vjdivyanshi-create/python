# Rock paper scissor game
import random
choices = ["rock", "paper", "scissor"]
while True:
    user_input = input("Enter your choice:")

    if user_input not in choices:
        print("Invalid choice, try again")
        continue    
    computer_choice = random.choice(choices)
    print(f"computer choice: {computer_choice}")

    if user_input == computer_choice:
        print("It's a tie!")    
    elif(user_input == "rock" and computer_choice == "scissor") or (user_input == "paper" and computer_choice == "rock") or (user_input == "scissor" and computer_choice == "paper"):
        print("You win!")

    else:
        print("Computer wins!")

    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != "y":
        break