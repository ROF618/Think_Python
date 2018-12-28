fin = open('word.txt')

def avoids(word, forbiden_letters):

    forbiden_letters = forbiden_letters.replace(',', '')
    for letter in word:
        for char in forbiden_letters:
            if char == letter:
                return print('does not work')
            else:
                continue
    print('this does work')


avoids("test", "e,a,b,c,d,")