fin = open('word.txt')


def avoids(word):
    #return true or false
    print("Please enter the characters you'd like to omit" + " (Please use the following format a,b,c)")
    forbiden_letters = input()
    forbiden_letters = forbiden_letters.replace(',', '')
    for letter in word:
        for char in forbiden_letters:
            if char == letter:
                #the return statement needs to contain logic for deleting the word from the list of words being iterated over
                return True
            else:
                continue
    return False

#the input function needs to go in the sort_words function so not to keep prompting for user input

def sort_words(words):
    for word in words:
        word.strip()
        if avoids(word):
            print(word)

sort_words(fin)