a = list(map(float, input().split()))

ans = "YES"
for i in range(1, len(a)):
    if a[i] <= a[i - 1]:
        ans = "NO"
        break

print(ans)


