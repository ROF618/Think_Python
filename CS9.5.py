def uses_all(word, required_letters):
    letters_in_word = []
    required_letters_list = []
    required_letters = required_letters.replace(',', '')
    for char in word:
        letters_in_word.append(char)

    letters_in_word = set(letters_in_word)

    for letters in required_letters:
        required_letters_list.append(letters)


    #the answer to this will be found in https://www.programiz.com/python-programming/methods/built-in/filter
    ## filter first and then use that mutated list to check against the required letters
    if letters_in_word.isdisjoint(set(required_letters_list)):
        print("it does not work")
    else:
        print("it does work")
uses_all("door", "d,o,r,e")