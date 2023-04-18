N = int(input())

d = dict()

for _ in range(N):
    word = input()
    lower_word = word.lower()
    if lower_word not in d:
        d[lower_word] = set()
        d[lower_word].add(word)
    else:
        d[lower_word].add(word)

task = list(map(str, input().split()))

errors = 0
for word in task:
    lower_word = word.lower()
    if lower_word in d:
        if word not in d[lower_word]:
            errors += 1
    else:
        count = sum(1 for ch in word if ch.isupper())
        if count != 1:
            errors += 1

print(errors)

