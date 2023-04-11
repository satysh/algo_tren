n = int(input())
seq = list(map(int, input().split()))

left = 0
rigth = len(seq) - 1

while left < rigth:
    if seq[left] == seq[rigth]:
        left += 1
        rigth -= 1
    else:
        left += 1

if left > rigth:
    left -= 1
    rigth += 1

#if left == rigth:
#    if (rigth + 1) < len(seq) and seq[left] == seq[rigth + 1]:
#        rigth += 1
#        left -= 1

count = len(seq[:left]) - len(seq[rigth + 1:])

ans = []
for i in range(count - 1, -1, -1):
    ans.append(seq[i])

print(count)
print(*ans)


# 5
# 1 2 1 2 2

# 11
# 1 1 1 1 1 1 1 1 1 1 1
