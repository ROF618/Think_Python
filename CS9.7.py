def consecutive_double_letters(word):
    letters_in_word = []
    i = 0
    for letter in word:
        letters_in_word.append(letter)
    while i < len(letters_in_word):
        if letters_in_word[i] == letters_in_word[i - 1]:
            print(len(letters_in_word)) #if this resolves to true you will need to add 2 to i to verify the consecutive part of this problem
        else:
            print(letters_in_word[i])
        i += 1


consecutive_double_letters("access")