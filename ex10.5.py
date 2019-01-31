def is_sorted(lineup):
    sorted_lineup = sorted(lineup)

    if lineup == sorted_lineup:
        return print("true")
    else:
        return print("false")

test = [2, 3, 5, 1, 4, 9, 7]
test1 = [1, 2, 3, 4]
is_sorted(test)