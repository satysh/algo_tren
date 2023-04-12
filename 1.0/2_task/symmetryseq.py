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
        rigth = len(seq) - 1

count = len(seq[:left + 1]) - len(seq[rigth:])
ans = []
for i in range(count - 1, -1, -1):
    ans.append(seq[i])

print(count)
print(*ans)

# 3
# 1 2 1

# 4
# 1 2 2 1

# 5
# 1 2 1 2 2

# 11
# 1 1 1 1 1 1 1 1 1 1 1

# 5
# 1 2 3 4 5

# 7
# 1 3 8 6 2 3 1

# 8
# 1 3 1 3 2 3 3 3

# 5
# 1 2 3 3 2