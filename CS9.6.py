def is_abecedarian(word):
    letters_in_word = []
    for letter in word:
        letters_in_word.append(letter)
    if letters_in_word == sorted(letters_in_word):
        print("it works")
    else:
        print("it doesn't work")

is_abecedarian("access")