N = int(input())
d = dict()

for _ in range(N):
    w, h = map(int, input().split())
    if w in d:
        if d[w] < h:
            d[w] = h
    else:
        d[w] = h

hcount = 0
for val in d.values():
    hcount += val

print(hcount)

