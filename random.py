import random

number = random.randint(1, 100)
for attempt in range(3):
    guess = int(input(f"Attempt {attempt + 1}: Guess the number (1-100): "))
    if guess == number:
        print("Correct!")
        break
    print("Too low!" if guess < number else "Too high!")
else:
    print(f"Sorry, the number was {number}.")
