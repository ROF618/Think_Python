def is_anagram(str1, str2):
    if set(str1) == set(str2):
        print("true")
    else:
        print("false")


is_anagram("arc", "rac")