# Write a program that helps people who look for a new job.
# The program receives the user's current monthly salary and a new job’s monthly salary.
# The program will calculate what is the difference of the annual salary between the old job and the new job,
# and will print the difference.
# For example, if currently I earn 8000 per month,
# and I consider taking a new job where I will earn 15000 per month,
# the program should print the following: “If you take the new job, you will earn 84000 more per year”

curr_salary = int(input("Insert your current monthly salary: "))
future_salary = int(input("Insert your future job salary: "))
annual_diff = (future_salary - curr_salary) * 12
print("If you take the new job, you will earn", annual_diff, "more per year")
