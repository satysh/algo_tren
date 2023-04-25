n, k = map(int, input().split())
x = list(map(int, input().split()))

xcntdict = {}
for xi in x:
    xcntdict[xi] = xcntdict.get(xi, 0) + 1

uniquex = list(xcntdict.keys())
uniquex.sort()

r = 0
ans = 0
dublicates = 0
for l in range(len(uniquex)):
    while r < len(uniquex) and uniquex[l] * k >= uniquex[r]:
        if xcntdict[uniquex[r]] >= 2:
            dublicates += 1
        r += 1

    rangelen = r - l

    ans += (rangelen - 1) * (rangelen - 2) * 3

    if xcntdict[uniquex[l]] >= 3:
        ans += 1

    if xcntdict[uniquex[l]] >= 2:
        dublicates -= 1
        ans += (rangelen - 1) * 3

    ans += dublicates * 3

print(ans)
