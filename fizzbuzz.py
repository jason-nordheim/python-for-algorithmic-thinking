# Fizz buzz: A game for two or more players
# Game Description:
# - Turn-based
# - Each turn, count aloud from 1 - 100
#     - each time you encounter a multiple of 3, replace it with the word "fizz"
#     - each time you encounter a multiple of 5, replace it with the word "buzz"
#     - each time you encounter a multiple of both 5 & 3 replace it with the word "fizz buzz"

fizz = 'fizz'
buzz = 'buzz'
fizz_buzz = fizz + buzz

for i in range(1, 101):
    divisible_by_three = i % 3 == 0
    divisible_by_five = i % 5 == 0
    if divisible_by_three and divisible_by_five:
        print(fizz_buzz)
    elif divisible_by_three:
        print(fizz)
    elif divisible_by_five:
        print(buzz)
    else:
        print(i)
