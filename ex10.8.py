#Write a function called has_duplicates that takes a list and returns True if there is any element that appears more than once. It should not modify the original list.

import random

def has_duplicates(OG_list):
    i = 0
#use the count method to determine if a item appears more than once in the list
    while i < len(OG_list):
       if OG_list.count(OG_list[i]) > 1:
           return print("true")
       i += 1

    print("false")


test = [1, 2, 3, 4, 5]
has_duplicates(test)

#part 2

#If there are 23 students in your class, what are the chances that two of you have the same
#birthday? You can estimate this probability by generating random samples of 23 birthdays and
#checking for matches. Hint: you can generate random birthdays with the randint function
#in the random module.


#Need to make the random int generated a set
i = 0
birthdays = []
while i < 23:
    birthdays.append(random.randint(1, 12))
    i += 1
print(birthdays)

