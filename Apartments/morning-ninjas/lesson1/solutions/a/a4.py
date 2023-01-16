#  Write a program that receives a name of the user and his age and prints his birth year.

name = input("Insert your name: ")
age = int(input("Insert your age: "))
print(f"{name} was born in {2022 - age}")
