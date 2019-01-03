fin = open("word.txt")

#function must return true if word contians only letters found in required letters
def uses_only(word, required_letters):
    for letter in word:
        for char in required_letters:
            if char == letter:
                #the return statement needs to contain logic for deleting the word from the list of words being iterated over
                return False
            else:
                continue
    return True