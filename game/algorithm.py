from random import randint

#create a list of play selections
selections = ["Rock", "Paper", "Scissors"]

def play_game(player_choice):
    # machine choice is randomented it can pick whatever from element 1 to 3 from position 0 to 2
    machine_choice = selections[randint(0,2)]
    
    if player_choice == machine_choice:
        return ("Result: { You: " + player_choice + ", Machine: "+ machine_choice + "}," + " Tie!-same selection with Machine play again")
    elif player_choice == "Rock":
        if machine_choice == "Paper":
            return ("Result: { You: " + player_choice + ", Machine: "+ machine_choice + "}," + "You lose! " + machine_choice + " covers " + player_choice)
        else:
            return ("Result: { You: " + player_choice + ", Machine: "+ machine_choice + "}, " +" You win!, " + player_choice +" smashes " + machine_choice)
    elif player_choice == "Paper":
        if machine_choice == "Scissors":
            return ("Result: { You: " + player_choice + ", Machine: "+ machine_choice + "}," +" You lose!, "+ machine_choice + " cut " + player_choice)
        else:
            return ("Result: { You: " + player_choice + ", Machine: "+ machine_choice + "}," + " You win!, " + player_choice + " covers " + machine_choice)
    elif player_choice == "Scissors":
        if machine_choice == "Rock":
            return ("Result: { You: " + player_choice + ", Machine: "+ machine_choice + "}," + " You lose... , " + machine_choice + " smashes " + player_choice)
        else:
            return ("Result: { You:" + player_choice + ", Machine: " + machine_choice + "}," + " You win!, " + player_choice +" cut " + machine_choice)
    else:
        return ("Error: That's not a valid play. Check your spelling!")


