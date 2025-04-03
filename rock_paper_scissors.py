from random import randint as ri

print("===================")
print("Rock Paper Scissors")
print("===================")

print("1 is for “✊” (Rock).")
print("2 is for “✋” (Paper).")
print("3 is for “✌” (Scissors).")

player_input = int(input("Enter the number from 1 to 3: "))
computer_input = ri(1, 3)

print("Player Input: ", player_input)
print("Computer Input: ", computer_input)

if(player_input>3 or player_input<1):
    print("Invalid Input")

if(player_input == computer_input):
    print("Draw")
elif(player_input == 1 and computer_input == 2):
        print("Computer Wins :(")
elif(player_input == 1 and computer_input == 3):
        print("YOU Won")
elif(player_input == 2 and computer_input == 1):
        print("YOU Won")
elif(player_input == 2 and computer_input == 3):
        print("Computer Wins :(")
elif(player_input == 3 and computer_input == 1):
        print("Computer Wins :(")
elif(player_input == 3 and computer_input == 2):
        print("YOU Won")
##END
