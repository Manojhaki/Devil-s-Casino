import random
total_steps = 20
current_steps = 0
price = ""
possible_rolls = 0


def devils_casino():
    print("Welcome to Devil's Casino")
    player_name = input("Give me your Name:")
    print("Ok ", player_name, ". You are now inside the Devil's Casino.")
    print("What is it that you desire ?")
    print("1> Name")
    print("2> Fame")
    print("3> Money")
    print("4> Wisdom")
    player_response = int(input("Pick one:"))
    global price
    global possible_rolls
    global current_steps

    if player_response == 1:
        price = "10 years of Life"
        possible_rolls = 4
    elif player_response == 2:
        price = "20 years of Life"
        possible_rolls = 3
    elif player_response == 3:
        price = "30 years of Life"
        possible_rolls = 2
    elif player_response == 4:
        price = "Eternity"
        possible_rolls = 1

    for x in range(0, possible_rolls):
        steps = random.randint(1, 20)
        print("Your", x+1, "dice rolled ", steps)
        current_steps = current_steps+steps
        print("You need ", total_steps-current_steps, " to go.")

    if current_steps >= total_steps:
        print("You Win. Here is your prize")
    else:
        print("You loose. Give me: ", price)


devils_casino()
