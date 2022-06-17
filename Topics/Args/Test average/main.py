def average_mark(*args):
    total = 0
    for i in args:
        total += i
    average = total / len(args)
    return round(average, 1)
