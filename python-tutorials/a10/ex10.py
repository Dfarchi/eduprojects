wins1 = 0
wins2 = 0
draws = 0

while True:
    answer = input("Do you want to play a game? (y/n)").lower()
    if answer == 'n':
        print(f"Total rounds played: {wins1 + wins2 + draws},\n"
              f"Total wins for player 1: {wins1},\n"
              f"total wins for player 2: {wins2},\n"
              f"draws: {draws}")
        print("bye-bye")
        exit(0)
    else:
        p1 = input("Player 1 turn (r - rock, s - scissors, p - paper): ")
        p2 = input("Player 2 turn (r - rock, s - scissors, p - paper): ")
        if p1 == p2:
            print("Draw")
            draws += 1
        elif p1 == "s":
            if p2 == 'r':
                print("2 wins")
                wins2 += 1
            else:
                print("1 wins")
                wins1 += 1
        elif p1 == "p":
            if p2 == "s":
                print("2 wins")
                wins2 += 1
            else:
                print("1 wins")
                wins1 += 1
        elif p1 == "r":
            if p2 == "s":
                print("1 wins")
                wins1 += 1
            else:
                print("2 wins")
                wins2 += 1