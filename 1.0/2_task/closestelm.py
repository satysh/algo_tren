n = int(input())
elms = list(map(int, input().split()))
x = int(input())

min_dist = float("inf")
ans = elms[0]

for elm in elms:
    curr_dist = abs(x - elm)
    if min_dist > curr_dist:
        min_dist = curr_dist
        ans = elm

print(ans)

# 5
# 1 2 3 4 5
# 6
