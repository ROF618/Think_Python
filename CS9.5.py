

def uses_all(word, required_letters):
    letters_in_word = []
    required_letters_list = []
    required_letters = required_letters.replace(',', '')
    required_letters = required_letters.replace(' ', '')
    required_letters = set(required_letters)
    for char in word:
        letters_in_word.append(char)
    letters_in_word = set(letters_in_word)
    for letters in required_letters:
        required_letters_list.append(letters)
    required_letters_list = set(required_letters_list)
    if set(letters_in_word) == required_letters_list:
        return print("it works")
    else:
        return print("it doesn't work")



uses_all("test", "t, e, s")