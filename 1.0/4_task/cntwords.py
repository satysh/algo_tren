file = open("input.txt", "r")

lines = file.readlines()
d = {}
for line in lines:
    words = line.split()
    for word in words:
        if word in d:
            print(d[word], end=" ")
            d[word] += 1
        else:
            print(0, end=" ")
            d[word] = 1

print()


