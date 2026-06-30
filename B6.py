#Build a number guessing game: the computer picks a random number 1–10, the user guesses until correct.
import random
num2 = random.randint(1,10)
while True :
    num = int(input("Enter a number between 1 and 10 = "))
    if num == num2:
        print("You guessed correctly ",num2)
        break
    else:
        print("try again")