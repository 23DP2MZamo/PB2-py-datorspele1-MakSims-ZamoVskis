import random
import time
options = ("rock", "paper", "scissors")
running = True

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")
    "rock" == """
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """
    
    "paper" == """
             _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
        """
    "scissors" == """
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        """
    

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:        
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("player izvelējās: ", "rock", "dators izvelējās: ", "scissors" )
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("You lose!")

    if not input("Play again? (y/n): ").lower() == "y":
        running = False

