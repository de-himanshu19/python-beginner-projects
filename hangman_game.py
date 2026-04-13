import random
word_list = [
            "apple", "tiger", "planet", "python", "garden",
            "rocket", "orange", "monkey", "school", "window",
            "bottle", "laptop", "pencil", "camera", "mobile",
            "bridge", "island", "desert", "forest", "ocean",
            "engine", "train", "flight", "market", "office",
            "doctor", "lawyer", "teacher", "artist", "driver"
            ]
secret_word = random.choice(word_list)
display_word = ["_"] * len(secret_word)
guess_word = []
attemts = 8

hangman = {
        1:
           """
              __________
              |   |
              |
              |
              |
              |
              |__________""",
        2: """
              __________
              |   |
              |   Ö
              |
              |
              |
              |__________""",
        3: """
              __________
              |   |
              |   Ö
              |  /
              |
              |
              |__________""",
        4: """
              __________
              |   |
              |   Ö
              |  /|
              |
              |
              |__________""",
        5: """
              __________
              |   |
              |   Ö
              |  /|>
              |
              |
              |__________""",
        6: """
              __________
              |   |
              |   Ö
              |  /|>
              |   |
              |
              |__________""",
        7: """
              __________
              |   |
              |   Ö
              |  /|>
              |   |
              |  /
              |__________""",
        8: """
              __________
              |   |
              |   X
              |  /|>
              |   |
              |  / >
              |__________"""
        }

print("!Welcome to hangman game!")

while attemts >0 and "_" in display_word:
  print(f"\nWord: {display_word}")
  print(f"Attempts left: {attemts}")
  guess = input("Guess a characer: ")
  if len(guess)!=1:
    print("!Please enter only one char!")
    continue

  if guess.isalpha() == False:
    print("!Please enter only characters!")
    continue

  if guess in guess_word:
    print("You already guessed the character ;)")
    continue

  guess_word.append(guess)
  print(f"your guess: {guess_word}")
  index = 0
  if guess in secret_word:
    while index < len(secret_word):
      if secret_word[index] == guess:
        display_word[index] = guess
        index +=1
      else:
        index +=1
    print("\n!Correct character, you guessed it right :)")
  else:
    print("\n! Wrong guess !")
    attemts -=1
    print(hangman[(8-attemts)])

if "_" not in display_word:
  print("\n! Congratulations ! U WON")
  print(f"\nThe word was: {secret_word}")
else:
  print("\n!No remaining attempts left !  YOU LOSE :(")
  print(f"\nThe word was: {secret_word}")