###Exercise set A
      while loops

1. Print First 10 natural numbers using while loop


2. Write a program that counts the total number of digits in a number received from a user using a while loop.


3. Reverse a given integer numer


5. Make a two-player Rock-Paper-Scissors game. Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game). In addition, keep track on amount of wins / draw for each round, and when the user chooses to exit your program, print all the statistics of the game - total rounds played, total wins for each player, total draws.

   ```
   Remember the rules:
   Rock beats scissors
   Scissors beats paper
   Paper beats rock
   ```

6. Write a program that receives student names and their grades one by one. The program should continue running until user inserts "$$$" to indicate end of input. After receiving "$$$", the program should print all the received data in pairs <Student name, Grade>. In addition the program should print an average grade.


5. Generate a random number between 1 and 100 (including 1 and 100). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: the following two lines will return you a random number between 1 and 10):
```
   import random
   random_num = random.randint(1, 10)
```
Keep the game going until the user types “exit”. Keep track of how many guesses the user has taken, and when the game ends, print this out.

### Exercise set B
      for loops
      range

1. Write a program that receives a number from a user and calculates the sum of all numbers from 1 to a given number

2. Write a program that receives a list of numbers, and prints the minimum number


3. Write a number that receives a list of numbers, and finds the second-largest number


4. Print list in reverse order using a loop


5. Get 10 dates from the user. The date is in the following format: dd.mm.yyyy (no need to check. After you got all the 10 dates, print the amount of dates in winter, autumn, sprint, summer, and print the dates themselves.

The output should look something like:

```
You entered 2 dates in winter:
11.12.2013
05.01.1999

You entered 8 dates in summer:
16.08.2012
05.07.1999

...
```

6. Find the factorial of a given number.
Take into account that factorial of 0 is 1, and factorial does not exist for negative numbers.


6. Write a program that receives a number from a user and prints multiplication table of a given number. For example:
   ```
   Insert a number: 5
   1*5 = 5
   2*5 = 10
   3*5 = 15
   4*5 = 20
   5*5 = 25
   6*5 = 30
   7*5 = 35
   8*5 = 40
   9*5 = 45
   10*5 = 50
   ```
_Bonus_: Use python formatting to format the output such that all the equations will be aligned for better readability, like this (such that all the '=' will appear one below other):
Hint: look for "padding numbers" using python format
```
Insert a number: 5
    1*5 = 5
    2*5 = 10
    3*5 = 15
    4*5 = 20
    5*5 = 25
    6*5 = 30
    7*5 = 35
    8*5 = 40
    9*5 = 45
   10*5 = 50

```



### Exercise set C
      nested loops

1. Write a program that receives rows number  and prints the following number pattern:
   ```
   1
   1 2
   1 2 3
   1 2 3 4
   1 2 3 4 5
   ```


2. Write a program to display all prime numbers within a range provided by user.
Note: A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers.


3. Write a program that receives a number from a user and prints the following start pattern. For example, for input 5, you should print:
```
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*

```
