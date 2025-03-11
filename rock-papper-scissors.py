import random

options = ("rock", "papper", "scissors")
running = True

while running:
        
    player = None
    computer = random.choice(options)


    while player not in options:
        player= input ("Enter a choice(rock, papper, csissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player  == computer:
        print("it's a tie!")
    elif player == "rock" and computer == "scissors":
        print("U win!")
        
    elif player == "papper" and computer == "scissors":
        print("U win!")
        
    elif player == "scissors" and computer == "papper":
        print("U win!")
    else:
        print("U lose!")

    play_again = input("Play again? (y/n): ").lower()
    if not play_again == "y":
        running = False
        
print("Thanks for playing :)")
        