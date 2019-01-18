def consecutive_double_letters(word):
    letters_in_word = []
    i = 0
    for letter in word:
        letters_in_word.append(letter)
    while i < len(letters_in_word):
        if letters_in_word[i] == letters_in_word[i - 1]:
            if letters_in_word[i - 2] == letters_in_word[i - 3]:
                if letters_in_word[i - 4] == letters_in_word[i - 5]:
                   return print("This works")
        i += 1
    print("this does not work")


consecutive_double_letters("Bookkeeper")