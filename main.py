import random
import time

print('''Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
You have 5 chances to guess the correct number.
''')

def the_game():
    game_difficulty = 0
    try:
        print('''Please select the difficulty level:
            1. Easy (10 chances)
            2. Medium (5 chances)
            3. Hard (3 chances)

    Enter your choice: ''')
        while True:
            game_difficulty = int(input())
            if game_difficulty in range(1, 4):
                match game_difficulty:
                    case 1:
                        game_difficulty = 10
                    case 2:
                        game_difficulty = 5
                    case 3:
                        game_difficulty = 3
                break

            else:
                print("Please select a number between 1 and 3.")
    except ValueError:
        print("Please enter a number.")

    difficulty_name = {
        10: "Easy",
        5: "Medium",
        3: "Hard",
    }
    print(f"Great! You have selected {difficulty_name[game_difficulty]} difficulty level.\n"
          f"Let's start the game!")

    random_num = random.randint(1, 100)
    attempts = 0
    start = time.time()
    while True:

        try:
            guess = int(input("Enter you guess: "))
            if guess == random_num:
                print(f"Congratulations! You guessed the correct number in {attempts} attempt" + f"{"s" if attempts != 1 else None}.")
                break
            elif guess < random_num:
                attempts += 1
                print(f"Incorrect! The number is greater than {guess}.")
            else:
                attempts += 1
                print(f"Incorrect! The number is less than {guess}.")

            if attempts == game_difficulty:
                print(f"You failed! All your {game_difficulty} attempts gone. GAME OVER")
                print(f"The number to guess was {random_num}.")
                break
        except ValueError:
          print("Please enter a number.")
    end = time.time()
    print(f"The guessing game took you PRECISELY {end-start} seconds of your precious lifetime.")
while True:
    the_game()
    user_input = input("Press any key to play again or q to quit.")
    if user_input == "q":
        break