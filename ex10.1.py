def nested_sum(ints):
    int_nested = []
    total = 0
    for num in ints:
        if num != int:
            for x in num:
                return x
        int_nested.extend(num)

    for single_int in int_nested:
        total += single_int
    print(total)



test = [1, 2, 3, 4, [22, 24, 25], 5, 6]
nested_sum(test)