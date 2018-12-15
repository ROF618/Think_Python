fin = open('word.txt')

def srch_word(words):
    for word in words:
        word.strip()
        if len(word) > 20:
            print(word)

srch_word(fin)
