n, r = map(int, input().split())

monuments = list(map(int, input().split()))

count = 0
left = right = 0

while right != n:
    distance = monuments[right] - monuments[left]
    if distance <= r:
        right += 1
    else:
        left += 1
        count += n - right

print(count)

# 10 54
# 11 38 46 49 57 59 62 65 67 72
