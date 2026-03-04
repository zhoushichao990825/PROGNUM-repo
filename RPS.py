import numpy as np
rng = np.random.default_rng()
def game(): # Defining the game function
    print("Welcome to the game of Rock,Paper,scissors!")
    print("Instructions: please input R for rock, P for paper and S for scissor") # Game rule
    player_input=str(input("R/P/S")) 
    RNG=rng.integers(low=1, high=4) #Let the computer input the 1-3 from RNG
    if RNG==1:
            computer_input="R"# Assigning each number generated with an answer
    elif RNG==2:
            computer_input="P"
    else:
            computer_input="S"
    print(f"your choise:{player_input}") # Adding context
    print(f"the computer chose:{computer_input}")
    if player_input==computer_input: # Judging the result
            print("Result: Tie") 
    elif player_input=="R" and computer_input=="S":
            print("Result: You Win")
    elif player_input=="P" and computer_input=="R":
            print("Result: You win")
    elif player_input=="S" and computer_input=="P":
            print("Result: You win")
    else:
            print("Result: You lose")
game()