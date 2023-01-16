names = []
grades = []
while True:
    name = input("Insert a name or $$$ to finish: ")
    if name == '$$$':
        break
    names.append(name)
    grade = int(input(f"Insert {name}'s grade: "))
    grades.append(grade)

print(f"Student names: {names}, total {len(names)}")
print(f"Grades average: {sum(grades)/len(grades)}")