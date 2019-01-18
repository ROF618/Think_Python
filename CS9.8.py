
def check_palindrome(numbers):
    num_list = []
    i = 0
    for digit in str(numbers):
        num_list.append(int(digit))
    num_list_reversed = list(reversed(num_list))
    while i < len(num_list):
        if num_list[i] == num_list_reversed[i]:
            print(num_list[i])

        i += 1


check_palindrome(5445)