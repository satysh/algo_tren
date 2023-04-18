import re

file = open("input.txt")
lines = file.readlines()
line = lines[0].split()
n = int(line[0])
C = line[1]
D = line[2]

keywords = set()
for i in lines[1:n + 1]:
    keywords.add(i.rstrip())

idents = {}
max_val = 0
queue = {}
counter = 0
for line in lines[n + 1:]:
    for word in re.split("[,():;{}% $#+-/*]", line):
        if word not in keywords and (not (D == "no" and word[0].isdigit())):
            char = ""
            if C == "no":
                word = word.lower()
            for sym in word:
                if sym.isalpha() or sym.isdigit() or sym == "_":
                    char = "".join([char, sym])
            if char != "":
                if char not in idents:
                    idents[char] = 1
                    queue[char] = counter
                    counter += 1
                else:
                    idents[char] += 1
                if idents[char] > max_val:
                    max_val = idents[char]

print(idents)
test = 0
for key, val in idents.items():
    if val == max_val and queue[key] > test:
        ans = key

print(ans)
