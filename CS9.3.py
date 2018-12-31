fin = open('word.txt')


def avoids(word, forbiden_letters):
    #return true or false
    for letter in word:
        for char in forbiden_letters:
            if char == letter:
                #the return statement needs to contain logic for deleting the word from the list of words being iterated over
                return False
            else:
                continue
    return True

#the input function needs to go in the sort_words function so not to keep prompting for user input

def sort_words(words):
    print("Please enter the characters you'd like to omit" + " (Please use the following format a,b,c)")
    forbiden_letters = input()
    forbiden_letters = forbiden_letters.replace(',', '')
    for word in words:
        word.strip()
        if avoids(word, forbiden_letters):
            print(word)
        else:
            continue

sort_words(fin)