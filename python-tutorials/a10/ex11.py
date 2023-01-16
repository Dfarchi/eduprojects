import random
random_num = random.randint(1, 100)
guess_cnt = 0

while True:
    guess = input("Insert your guess: ")
    if guess == "exit":
        print("Total guess count:", guess_cnt, "Bye-bye!")
        break
    else:
        guess_cnt += 1
        guess = int(guess)
        if guess == random_num:
            print(f"You guessed it! Total guess number: {guess_cnt}")
            break
        elif guess < random_num:
            print("Too small")
        else:
            print("Too big")
