file = open("input.txt")
text = file.readlines()

words_set = set()
for sens in text:
    for word in sens.split():
        words_set.add(word)

print(len(words_set))
