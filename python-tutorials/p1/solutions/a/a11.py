# Same as previous (11), but this time you get the time in seconds,
# and you should display the length in the format hh:mm:ss

total_seconds = int(input("Insert movie length in seconds: "))
total_minutes = total_seconds // 60
seconds = total_seconds % 60
hours = total_minutes // 60
minutes = total_minutes % 60

print(f"The length of the movie is: {hours}:{minutes}:{seconds}")