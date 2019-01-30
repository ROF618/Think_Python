def nested_sum(ints):
    #int_nested = []
    for num in ints:
        if num != int:
            for x in list(num):
                print(x)
        print(num)



test = [1, 2, 3, 4, [22, 24, 25], 5, 6]
nested_sum(test)