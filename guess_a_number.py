import random
computer_number = random.randint(1, 100)
counter = 0
while True:
    player_guess = int(input("Which number do you think the computer picked? [1 - 100]  "))
    if player_guess == computer_number:
        print(f"Good job, the computer number was {computer_number}")
        print(f"You guessed the correct number in {counter} tries")
    elif player_guess < computer_number:
        counter += 1
        print("\033[0;32m""Higher.""\033[0m")
    elif player_guess > computer_number:
        counter += 1
        print("\033[0;31m""Lower.""\033[0m")
    else:
        print("Invalid input, try again.")
        continue


