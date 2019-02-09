#Two words are anagrams if you can rearrange the letters from one to spell the other. Write a function called is_anagram that takes two strings and returns True if they are anagrams.

def is_anagram(word1, word2):
    word1_list = []
    word2_list = []
    for lett in word1:
        word1_list.append(lett)

    for char in word2:
        word2_list.append(char)


    print(list(reversed(word1_list)))
    print(word2_list)


is_anagram('car', 'mace')
