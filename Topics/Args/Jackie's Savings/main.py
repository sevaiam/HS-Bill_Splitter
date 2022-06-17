def final_deposit_amount(*args, amount=1000):
    earn = amount
    for i in args:
        earn += earn * i / 100
    return round(earn, 2)
