from_unit = input("Insert a unit to convert from: ")
to_unit = input("Insert a unit to convert to: ")
amnt = float(input("Insert amount of storage: "))

# calculate amount of "steps" to take
steps = None
if from_unit == to_unit:
    steps = 0
if from_unit == 'bytes' and to_unit == 'kb' or \
        from_unit == 'kb' and to_unit == 'mb' or \
        from_unit == 'mb' and to_unit == 'gb' or \
        from_unit == 'gb' and to_unit == 'tb':
    steps = -1
if from_unit == 'bytes' and to_unit == 'mb' or \
        from_unit == 'kb' and to_unit == 'gb' or \
        from_unit == 'mb' and to_unit == 'tb':
    steps = -2
if from_unit == 'bytes' and to_unit == 'mb' or \
        from_unit == 'kb' and to_unit == 'tb':
    steps = -3
if from_unit == 'bytes' and to_unit == 'tb':
    steps = -4
if from_unit == 'kb' and to_unit == 'bytes' or \
        from_unit == 'mb' and to_unit == 'kb' or \
        from_unit == 'gb' and to_unit == 'mb' or \
        from_unit == 'tb' and to_unit == 'gb':
    steps = 1
if from_unit == 'mb' and to_unit == 'bytes' or \
        from_unit == 'gb' and to_unit == 'kb' or \
        from_unit == 'tb' and to_unit == 'mb':
    steps = 2
if from_unit == 'gb' and to_unit == 'bytes' or \
        from_unit == 'tb' and to_unit == 'kb':
    steps = 3
if from_unit == 'tb' and to_unit == 'bytes':
    steps = 4

if not steps:
    print("Invalid input, can't convert")
else:
    result = amnt * (1024 ** steps)
    print(result)