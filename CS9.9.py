def reversed_age(age_A, age_B):
    age_A = set(age_A)
    age_B = set(age_B)

    if age_A == age_B:
        return print(age_A, age_B)
    else:
        return print("it does not work")


def find_pali_age(start_age1, start_age2):
    start_age1_range = []
    start_age2_range = []
    i = 0

    for age1 in range(start_age1, 100):
        start_age1_range.append(age1)

    for age2 in range(start_age2, 100):
        start_age2_range.append(age2)

    while i < (len(start_age1_range) or len(start_age2_range)):
        #print(start_age2_range[i])
        reversed_age(str(start_age1_range[i]), str(start_age2_range[i]))
        i += 1
    print(reversed_age(start_age1_range, start_age2_range))


find_pali_age(37, 73)