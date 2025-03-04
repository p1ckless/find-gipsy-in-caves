import random  # Library random

game_name = "Find GIPSY"


difficulty = input("Choose Difficulty! [EASY/NORMAL/HARD]: ").lower()

if difficulty == "easy":
    main_caves = random.randint(3, 5)
    health = 5
elif difficulty == "normal":
    main_caves = random.randint(6, 8)
    health = 3
elif difficulty == "hard":
    main_caves = random.randint(9, 
    print("Invalid Choice, Defaulting to Normal Difficulty!")
    main_caves = random.randint(6, 8)
    health = 3

while True:
    caves_o = "[_]"
    caves_empty = [caves_o] * main_caves  # Membuat daftar gua
    gipsy_position = random.randin(1, main_caves)

    caves_empty_string = " ".join(caves_empty)
    print(f"\nTake a look at these caves: {caves_empty_string}")
    print(f"You have {health} Health!\n")

    # Main game loop
    while health > 0:
        try:
            user_choice = int(input(f"Which cave do you think GIPSY is in? [1 - {main_caves}]: "))

            if user_choice < 1 or user_choice > main_caves:
                print(f"Please choose a number between 1 and {main_caves}!")
                continue  # the code will ask again for valid input 

            # The new GIPSY position
            caves = caves_empty.copy()
            caves[gipsy_position - 1] = "[🤖]"
            caves_empty_string = " ".join(caves)
import random  # Library random

game_name = "Find GIPSY"


difficulty = input("Choose Difficulty! [EASY/NORMAL/HARD]: ").lower()

if difficulty == "easy":
    main_caves = random.randint(3, 5)
    health = 5
elif difficulty == "normal":
    main_caves = random.randint(6, 8)
    health = 3
elif difficulty == "hard":
    main_caves = random.randint(9, 12)
    health = 1
else:
    print("Invalid Choice, Defaulting to Normal Difficulty!")
    main_caves = random.randint(6, 8)
    health = 3

while True:
    caves_o = "[_]"
    caves_empty = [caves_o] * main_caves  # Membuat daftar gua
    gipsy_position = random.randint(1, main_caves)

    caves_empty_string = " ".join(caves_empty)
    print(f"\nTake a look at these caves: {caves_empty_string}")
    print(f"You have {health} Health!\n")

    # Main game loop
    while health > 0:
        try:
            user_choice = int(input(f"Which cave do you think GIPSY is in? [1 - {main_caves}]: "))

            if user_choice < 1 or user_choice > main_caves:
                print(f"Please choose a number between 1 and {main_caves}!")
                continue  # the code will ask again for valid input 

            # The new GIPSY position
            caves = caves_empty.copy()
            caves[gipsy_position - 1] = "[🤖]"
            caves_empty_string = " ".join(caves)

            if user_choice == gipsy_position:
                print(f"{caves_empty_string} Congratulations, you found GIPSY!\n")
                break  # leave the loop if user win
            else:
                health -= 1
                print(f"{caves_empty_string} Wrong guess! GIPSY was in cave {gipsy_position}\n")
                print(f"Your health left is {health}\n")

            
            if health == 0:
                print("Game Over! Nice Try.")

        except ValueError:
            print("Invalid Input! Please enter a number.")

    # ask user to play again
    play_again = input("Do you want to play again? [Y/N]:\n ").lower()
    if play_again == "n":
        break


print("Thank you for playing!\n")
print("""Regards,
pickless! :)\n""")
            if user_choice == gipsy_position:
                print(f"{caves_empty_string} Congratulations, you found GIPSY!\n")
                break  # leave the loop if user win
            else:
                healueError:
            print("Invalid Input! Please enter a number.")

    # ask user to play again
    play_again = input("Do you want to play again? [Y/N]:\n ").lower()
    if play_again == "n":
        break


print("Thank you for playing!\n")
print("""Regards,
pickless! :)\n""")
