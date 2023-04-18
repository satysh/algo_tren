file = open("input.txt")
lines = file.readlines()
line = lines[0].split()
n = int(line[0])
C = line[1]
D = line[2]

keywords = set()
for i in lines[1:n + 1]:
    if C == "no":
        i = i.lower()
    keywords.add(i.rstrip())

idents = {}
max_val = 0
queue = {}
counter = 0
for line in lines[n + 1:]:
    word = []
    symcnt = 0
    for sym in line:
        if sym.isalpha() or sym.isdigit() or sym == "_":
            word.append(sym)
            if sym.isalpha() or sym == "_":
                symcnt += 1
        elif symcnt > 0:
            if word and (not (D == "no" and word[0].isdigit())):
                new_word = "".join(word)
                if C == "no":
                    new_word = new_word.lower()
                if new_word not in keywords:
                    if new_word not in idents:
                        idents[new_word] = 1
                        queue[new_word] = counter
                        counter += 1
                    else:
                        idents[new_word] += 1
                    if idents[new_word] > max_val:
                        max_val = idents[new_word]
            word = []
        else:
            word = []


test = float("inf")
ans = ""
for key, val in idents.items():
    if val == max_val and queue[key] < test:
        ans = key
        test = queue[key]

print(ans)
