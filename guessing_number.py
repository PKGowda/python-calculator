import random
guess = int(input("Enter a number between 1 and 10: "))
number = random.randint(1,10)
if guess == number:
    print("Correct guess!")
else:
    print("Wrong guess! The number was", number)
