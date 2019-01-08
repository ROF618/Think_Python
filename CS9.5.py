

def uses_all(word, required_letters):
    letters_in_word = []
    required_letters_list = []
    required_letters = required_letters.replace(',', '')
    final_list = []
    for char in word:
        letters_in_word.append(char)

    letters_in_word = set(letters_in_word)

    for letters in required_letters:
        required_letters_list.append(letters)
    #the answer to this will be found in https://www.programiz.com/python-programming/methods/built-in/filter
    ## filter first and then use that mutated list to check against the required letters
    for required_letters_list in letters_in_word:
        if required_letters_list == letters_in_word:
            final_list.append(required_letters_list)
    if letters_in_word == final_list:
        return print("it works")
    else:
        return print("it doesn't work")



uses_all("test", "t, e, s")