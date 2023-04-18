file = open("input.txt", "r")

d = dict()
maxc = 0
for line in file.readlines():
    words = line.split()
    for word in words:
        d[word] = d.get(word, 0) + 1
        if d[word] > maxc:
            maxc = d[word]

for word, cnt in sorted(d.items()):
    if cnt == maxc:
        print(word)
        break



