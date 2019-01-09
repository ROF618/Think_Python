

def uses_all(word, required_letters):
    letters_in_word = []
    required_letters_list = []
    final_list = 0
    required_letters = required_letters.replace(',', '')
    required_letters = required_letters.replace(' ', '')
    required_letters = set(required_letters)
    print(required_letters)
    for char in word:
        letters_in_word.append(char)

    letters_in_word = set(letters_in_word)

    for letters in required_letters:
        required_letters_list.append(letters)
    #the answer to this will be found in https://www.programiz.com/python-programming/methods/built-in/filter
    ## filter first and then use that mutated list to check against the required letters


    if set(letters_in_word) == required_letters_list:
        return print(len(letters_in_word))
    else:
        return print(letters_in_word, required_letters_list, final_list)



uses_all("test", "t, e, s")