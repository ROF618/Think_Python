fin = open('word.txt')
def has_no_e(words):
    word_with_e = []
    all_words = []
    for word in words:
        seperate_word = word.strip()
        all_words.append(seperate_word)
        for letter in seperate_word:
            if letter == "e":
                word_with_e.append(seperate_word)

            else:
                continue
    percent_of_e = (len(word_with_e)/len(all_words)) * 100
    print(all_words)
    print(str(round(percent_of_e)) + "%" + " of words contain the letter E")


has_no_e(fin)