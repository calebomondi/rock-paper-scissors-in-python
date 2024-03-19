import random

print("WELCOME TO ROCK-PAPER-SCISSORS GAME")

options = ['R','P','S']

comp_score = 0
player_score = 0
round = 1

limit = input("How many times do yout want to play? ")
if limit.isdigit() and limit != '0':
    limit = int(limit)
    while round < limit+1:
        print(f"\nRound {round}")
        user_input = input("Enter rock(r), paper(p) or scissors(s) to play or (q) to quit: ")

        if user_input.upper() == 'Q':
            print("GOODBYE!")
            quit()

        if user_input.upper() not in options:
            print("Play with correct letters R, P or S or q to quit")
            continue

        rand_num = random.randint(0,2)
        #Rock(R) - 0, Paper(P) - 1, Scissors(S) - 2
            
        comp_input = options[rand_num]

        print(f" You: {user_input.upper()}")
        print(f"comp: {comp_input}")

        if user_input.upper() == 'R' and comp_input == 'S':
            print("You win!")
            player_score += 1
        elif user_input.upper() == 'S' and comp_input == 'P':
            print("You win!")
            player_score += 1
        elif user_input.upper() == 'P' and comp_input == 'R':
            print("You win!")
            player_score += 1
        elif user_input.upper() == comp_input:
            print("Its a tie!")
        else:
            print("Computer wins!")
            comp_score += 1
        
        round += 1
    
    print(f"\nYou have scored {player_score}")
    print(f"The computer scored {comp_score}")
    print(f"Number of ties  {round - (player_score + comp_score + 1)}")
    if comp_score > player_score:
        print("\nThe computer wins this match!")
        print("Play a rematch to prove your are the master!\n")
    elif comp_score == player_score:
        print("\nYou have matched the computers strength, you are a shifu!\n")
    else:
        print("\nYou have won this match, kudos!\n")
else:
    print("Enter values that is a digit and is greater than 0!")

