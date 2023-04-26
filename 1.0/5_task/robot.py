from collections import deque

k = int(input())
operations = input()

ans = 0
l = 0
r = k
mem = deque(operations[l:r], k)
for l in range(len(operations) - k):
    i = 0
    j = r
    flag = False
    while j < len(operations) and mem[i] == operations[j]:
        flag = True
        j += 1
        i += 1
        if i == len(mem):
            i = 0
    if flag:
        curlen = j - l
        ans += curlen - k

    if r < len(operations):
        mem.append(operations[r])
    r += 1


print(ans)
