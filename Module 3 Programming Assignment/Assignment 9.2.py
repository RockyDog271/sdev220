def get_odds():
    odds = []
    ValueRange = range(1, 10)
    for i in ValueRange:
        if i % 2 != 0:
            odds.append(i)
    return odds

odds = get_odds()
# use a for loop? okay?
oddcount = 0
for i in odds:
    oddcount += 1
    if oddcount == 3:
        print(i)
        quit()