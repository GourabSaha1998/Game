import random

print("Welcome to the gueessing game.")
print("To play you need to guess a number between 0 and 100. The programme will tell you whether you are cold or warm.")
print("If you get within 10 from the number you will be warm.")


while True:

    a = random.randint(0,101)

    guesses = [0]



    try:
        guess = int(input("Please enter a number: "))

        if 0 < guess < 101 and guess == a:
            print("Well done! You guessed correctly!")
            break
        elif 0 < guess < 101 and guess in range(a, a+10) or range(a, a-10):
            print("WARM")
            continue
        elif 0 < guess < 101 and guess not in range(a, a+10) or range(a, a-10):
            print("COLD")
            continue
        elif 0 > guess or 101 < guess:
            print("Your guess is invalid")
            continue
    except ValueError:
            print("Your guess is invalid")
            continue

    
