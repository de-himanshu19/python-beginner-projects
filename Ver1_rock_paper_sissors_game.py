#rock paper sissors game
# Rock (1) beats sissor (3)
# sissor (3) cuts paper (2)
# paper (2) wraps rock (1)

# VERSION 1: code made by using simple logic


import random

rps = {1: "Rock",
       2: "Paper",
       3: "Sissor"
      }
comp_value = random.randint(1,3)
user_value = int(input("""!Welcome to Rock Paper Sissors game!
you are playing against computer...
1. Rock
2. Paper
3. Sissor
Please enter your choice : """))

print(f"\n CPU chose : {rps[comp_value]}\n&\n you chose : {rps[user_value]}\n")
if(user_value == 1 and comp_value == 3):
  print("!!ROCK crush SISSOR!!       YOU WIN")
elif(user_value == 1 and comp_value == 2):
  print("!!PAPER wraps ROCK!!       YOU LOSE")
elif(user_value == 3 and comp_value == 2):
  print("!!SISSOR cuts PAPER!!       YOU WIN")
elif(user_value == 3 and comp_value == 1):
  print("!!ROCK crush SISSOR!!       YOU LOOSE")
elif(user_value == 2 and comp_value == 1):
  print("!!PAPER wraps ROCK!!       YOU WIN")
elif(user_value == 2 and comp_value == 3):
  print("!!SISSOR cuts PAPER!!       YOU LOOSE")
else:
  print("!! Its a draw, you both choose same !!")