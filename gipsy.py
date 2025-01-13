import random # library random
game_name = "Find  GIPSY"

while True:
    caves_o = "[_]"
    caves_empty = [caves_o] * 4  # caves
    gipsy_position = random.randint(1, 4)

    caves = caves_empty.copy()  # GIPSY Position
    caves[gipsy_position - 1] = "[🤖]"

    caves_empty = " ".join(caves_empty)
    caves = " ".join(caves)

    print(f"take a look at these caves {caves_empty}")

    # main code
    while True:  # Loop to keep asking user if the answer valid 
        try:
            user_choice = int(input("""Which cave do you think GIPSY is in there? [1 / 2 / 3 /4]: """))
            if user_choice < 1 or user_choice > 4:
                print("Please choose number between 1 - 4!")
                print(f"Please choose again, take a look at these caves {caves_empty}")
                continue  # Loop to ask user for valid number 

            if user_choice == gipsy_position:
                print(f"{caves} Congratulation, you found GIPSY!")
                break  # Automatic exit the Loop if user succes to find GIPSY
            else:
                print(f"{caves} Upss, wrong guess, GIPSY is hiding in cave {gipsy_position}.")
                break  # Automatic exit the Loop if user fail to find GIPSY
        except ValueError:
            print("Please choose number between 1 - 4!")
            print(f"Please choose again, take a look at these caves {caves_empty}")
            continue  # Another Loop

    play_again = input(f"Do you want to play again? [Y/N]: ")
    if play_again.lower() == "n":
        break

# if user chooses n
print(f"""Thank you for playing :)
Regards,
p1ickless""")
