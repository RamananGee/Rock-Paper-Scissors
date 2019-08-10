import random
player_wins=0
computer_wins=0
wining_score=3


while(player_wins < wining_score and computer_wins < wining_score):
    print(f"Player Score: {player_wins} Computer Score: {computer_wins}")
    print("Rock....")
    print("Paper....")
    print("Scissors...")

    player=input("player,make your move: ").lower()
    if player == "quit" or player == "q":
        break 

    rand_num = random.randint(0,2)
    if rand_num == 0:
        computer = "rock"
    elif rand_num == 1:
        computer = "paper"   
    else:
        computer = "scissors"
    print("computer make your move:",computer)


    if player == computer :
        print("It is a Tie")
    elif player == "rock":
        if computer == "scissors":
            print("player wins!")
            player_wins=player_wins+1
        else: 
            print("computer wins!")
            computer_wins=computer_wins+1
    elif player == "paper":
        if computer == "rock":
            print("player, wins!")
            player_wins=player_wins+1
        else:
            print("computer, wins!")
            computer_wins=computer_wins+1
    elif player == "scissors":
        if computer =="paper":
            print("player, wins!")
            player_wins=player_wins+1
        else:
            print("computer, wins!")
            computer_wins=computer_wins+1

    else:
        print("Please Enter a valid move!")
if player_wins>computer_wins:
    print("CONGRATS,YOU WON!")
elif player_wins == computer_wins:
    print("IT IS A TIE")    
else:
    print("OH NO! COMPUTER WON")    
print(f"FINAL SCORE.....Player Score: {player_wins} Computer Score: {computer_wins}")
        

