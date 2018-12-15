fin = open('word.txt')

print(fin.readline())
print(fin.readline())

line = fin.readline()
word = line.strip()

print(word)