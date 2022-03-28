import random

# choices = ['r','p','s']

# def check_winner(player_choice, com_choice):
#     if player_choice == "r" and com_choice=='s':
#         return "Player Wins"
#     elif player_choice == "p" and com_choice=='r':
#         return "Player Wins"
#     elif player_choice == "s" and com_choice=='p':
#         return "Player Wins"
#     elif player_choice == "s" and com_choice=='r':
#         return "Computer Wins"
#     elif player_choice == "r" and com_choice=='p':
#         return "Computer Wins"
#     elif player_choice == "p" and com_choice=='s':
#         return "Computer Wins"
#     else:
#         return "It's a tie!"
    


# print("Welcome to rock, paper, scissors.\nEnter R for Rock, P for Papper and S for Scissors.")

# player_choice = input(">").lower()
# com_choice = random.choice(choices)
# if player_choice in choices:
#     result = check_winner(player_choice, com_choice)

#     print(result)
#     print(f"Computer selected {com_choice}")
    
# else:
#     print("Invalid Input!")


# h = 1
# while h <= 10:
#     if h == 10:
#         print("Boom")
#     else:
#         print(h)
        
#     h+=1
# i = 1
# while True:
    
#     print(f"Keep playing {i}")
#     c = input("Continue?\n>")
#     if c == "y":
#         i+=1
#         continue
#     else:
#         break
    
    

score = 0
trial = 5

def game():
    a = [3,2,5,6,8,7]
    print(f"Select any number from {a}.\nWe hope it doesn't end in tears.\n")
    com_choice = random.choice(a)
    random.shuffle(a)
    print("Guess the number:")
    user_choice = int(input(">"))

    if user_choice in a:
        if user_choice == com_choice:
            global score
            global trial
            trial +=1
            score+=2
            print("Correct!")
            print(f"{trial} trial(s) remaining!")
            
        else:
            print("Incorrect")
            print(f"{trial} trial(s) remaining!")
    else:
        print("Comerade no be so!")
        print(f"{trial} trial(s) remaining!")
        
while True:
    while trial >0:
        trial -=1
        game()
    print("Game over")
    print(f"Your score is {score}\n")  
     
    print("\nDo you want to try again?(Y/n)")
    choice = input(">").lower()
    if choice == 'y':
        continue
    else:
        break

    
    

