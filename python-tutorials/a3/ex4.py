# 4. Make a two-player Rock-Paper-Scissors game.
# Ask for player plays (using input), compare them, print out a message of congratulations to the winner.
# Remember the rules:
# Rock beats scissors
# Scissors beats paper
# Paper beats rock

p1 = input("Player 1 turn (r - rock, s - scissors, p - paper): ")
p2 = input("Player 2 turn (r - rock, s - scissors, p - paper): ")
if p1 == p2:
    print("Draw")
elif p1 == "s":
    if p2 == 'r':
        print("2 wins")
    else:
        print("1 wins")
elif p1 == "p":
    if p2 == "s":
        print("2 wins")
    else:
        print("1 wins")
elif p1 == "r":
    if p2 == "s":
        print("1 wins")
    else:
        print("2 wins")
