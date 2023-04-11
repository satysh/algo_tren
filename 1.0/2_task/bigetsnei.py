a = list(map(float, input().split()))
counter = 0

for i in range(1, len(a) - 1):
    if a[i] > a[i - 1] and a[i] > a[i + 1]:
        counter += 1

print(counter)

# 1 2 3 4 5
# 5 4 3 2 1
# 1 5 1 5 1

