k = int(input())
operations = input()

ans = 0
curlen = 0
for r in range(k, len(operations)):
    if operations[r] == operations[r - k]:
        curlen += 1
        ans += curlen
    else:
        curlen = 0

print(ans)



'''
k = int(input())
operations = input()

ans = 0
l = 0
r = k
while r < len(operations):
    i = 0
    flag = False
    while r < len(operations) and operations[l + i] == operations[r]:
        flag = True
        r += 1
        i += 1
        if i == k:
            i = 0
    if flag:
        curlen = r - l
        ans += (curlen - k + 1) * (curlen - k) // 2
    else:
        r += 1

    l = r - k

print(ans)
'''
