n = int(input())
botms = list(map(int, input().split()))
d = dict()
k = int(input())
seq = list(map(int, input().split()))


for i in range(n):
    d[i + 1] = botms[i]

for sym in seq:
    if sym in d:
        d[sym] -= 1

for botm in range(1, n + 1):
    if d[botm] < 0:
        print("YES")
    else:
        print("NO")

