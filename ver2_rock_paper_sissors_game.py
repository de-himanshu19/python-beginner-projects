#rock paper sissors game
# Rock (1) beats sissor (3)
# sissor (3) cuts paper (2)
# paper (2) wraps rock (1)

#Advanced version using dictinary and game rules defined under rules dict as tuples 

import random

rps = {
    1: "Rock",
    2: "Paper",
    3: "Scissors"
}

wins_against = {
    1: 3,
    2: 1,
    3: 2
}

rules = {
    (1, 3): "Rock crushes Scissors",
    (3, 2): "Scissors cuts Paper",
    (2, 1): "Paper wraps Rock"
}

user_value = int(input("Enter 1 for Rock, 2 for Paper, 3 for Scissors: "))
comp_value = random.randint(1, 3)

print(f"\nCPU chose: {rps[comp_value]}")
print(f"You chose: {rps[user_value]}\n")

if user_value == comp_value:
    print("It's a draw!")
elif wins_against[user_value] == comp_value:
    print(f"{rules[(user_value, comp_value)]} → YOU WIN")
else:
    print(f"{rules[(comp_value, user_value)]} → YOU LOSE")