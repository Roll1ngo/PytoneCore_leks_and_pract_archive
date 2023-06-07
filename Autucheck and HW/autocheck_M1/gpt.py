import random

print("Dice Rolling Simulator")
print("")


# ask user for number of dice rolls
# num_rolls = int(input("How many times would you like to roll the dice? "))


# define function for rolling a single die
def roll_die():
    return random.randint(1, 6)


# roll the dice the specified number of times
for number in range(15):
    roll1 = roll_die()
    roll2 = roll_die()
    print("Roll", number + 1, ": [", roll1, ",", roll2, "]")


print("")
print("Thanks for using the dice rolling simulator!")
