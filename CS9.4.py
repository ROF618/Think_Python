fin = open("word.txt")

#function must return true if word contians only letters found in required letters
def uses_only(word, required_letters):
    # make the for loop break the word out into single characters and then we will check they match required letters
    broken_down_word = []
    required_letters_list = []
    required_letters = required_letters.replace(',', '')
    for letter in word:
        broken_down_word.append(letter)

    for char in required_letters:
        required_letters_list.append(char)

    #the if statement is not correct it needs to be tweaked so that if there are repeating letters the function will still return true as long as those letters are present at least once in the word
    if broken_down_word == required_letters_list:
        return print('it works')
    print(broken_down_word)
    print(required_letters_list)

uses_only('door', 'd,o,r')