#Write a function called has_duplicates that takes a list and returns True if there is any element that appears more than once. It should not modify the original list.

def has_duplicates(OG_list):
    i = 0
#use the count method to determine if a item appears more than once in the list
    while i < len(OG_list):
       OG_list.count(OG_list[i])
        i += 1

    print("false")

test = [1, 2, 3, 4, 5]
has_duplicates(test)