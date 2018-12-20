fin = open('word.txt')

def avoids(words, omit_this):
    omit_this = []
    all_words = []
    for word in words:
        seperate_word = word.strip()
        all_words.append(seperate_word)
    for word in all_words:
        if word == omit_this:
            print(word)

avoids(fin, a)