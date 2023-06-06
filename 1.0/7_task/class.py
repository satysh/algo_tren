n, d = map(int, input().split())
x = list(map(int, input().split()))

sorted_x = sorted(x)
ans_dict = {}

r = 0
max_n = 0
for l in range(len(sorted_x)):
	while r < len(sorted_x) and (sorted_x[r] - sorted_x[l]) <= d:
		r += 1
	max_n = max(max_n, r - l)

cnt = 0
for sorted_xi in sorted_x:
	cnt += 1
	ans_dict[sorted_xi] = cnt
	if cnt == max_n:
		cnt = 0

print(max_n)
for xi in x:
	print(ans_dict[xi], end=' ')
print()
