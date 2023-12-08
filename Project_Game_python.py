import random


#roll function

def roll():
    min_value=1
    max_value=6
    roll=random.randint(min_value,max_value)
    return roll


# Enter the value here !!!

while True:
    players=input("Enter the number of the players (2-4) :")
    if players.isdigit():
        players=int(players)
        if 2 <=players <=4:
            print("Must be between 2-4")
            break
        else:
            print("Invalid, try again")



#max score here 


max_score=50
players_score=[0 for _ in range (players)]

while max(players_score) < max_score:
    for player_index in range(players):
        print("\nPlayer",player_index +1,"turn has just started!\n")
        print("Your total score is :",players_score[player_index],"\n")
        current_score=0

        while True:
            should_roll=input("Would you like to roll (y)>")
            if should_roll.lower() != "y":
                break
            
            value=roll()
            if value == 1:
                print("You rolled a 1! Turn done")
                current_score=0
                break
            else:
                current_score += value
                print("You rolled a :",value)
            print("Your score is :",current_score)
        players_score[player_index]+= current_score


        print("Your total score is :",players_score[player_index])


max_score=max(player_score)
wining_index=player_score.index(max_score)
print("Player number",winning_index + 1,"is the winner with a score of:",max_score)

            
        
