from random import randint
target_number = randint(0, 999)
attempts = randint(5, 10)
print(target_number)
print(f"I guessed my number! \nI give you {attempts} chances!")
lowest_possible_range = 0
highest_possible_range = 999

for i in range(1, attempts+1):
    try:
        guessed_number = int(input(
            f"\nRange: ({lowest_possible_range}, {highest_possible_range})\nYour guess: "))
    except ValueError:
        print("Please enter a valid integer.")
        continue
    if (guessed_number > target_number):
        print("Lower!")
        if (guessed_number >= highest_possible_range):
            print(
                "You already know highest range is lower than your current guess!")
        else:
            highest_possible_range = guessed_number

    elif (guessed_number < target_number):
        print("Higher!")
        if (guessed_number <= lowest_possible_range):
            print(
                "You already know lowest range is higher than your current guess!")
        else:
            lowest_possible_range = guessed_number

    else:
        print(
            f"Yes you won! You guessed the random number in {i} tries!")
        break
    print(f"You have {attempts-i} chances remaining!")
else:
    print(f"You lost, my guessed number was {target_number}")
