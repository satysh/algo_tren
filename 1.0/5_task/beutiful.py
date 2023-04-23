N, K = map(int, input().split())

trees = list(map(int, input().split()))

left = right = 0
min_len = float('inf')
ans_left = 0
ans_right = N -1
trees_dict = {}

while right < N:
	while right < N and len(trees_dict) < K:
		trees_dict[trees[right]] = trees_dict.get(trees[right], 0) + 1
		right += 1

	flag = False
	while left < N and len(trees_dict) == K:
		flag = True
		trees_dict[trees[left]] -= 1
		if trees_dict[trees[left]] == 0:
			trees_dict.pop(trees[left])
		left += 1

	if flag and min_len > (right - left + 1):
		min_len = right - left + 1
		ans_left = left  
		ans_right = right


print(ans_left, ans_right)

# 16 4
# 1 2 3 2 3 4 2 3 2 1 2 3 3 4 1 2

# 6 6
# 2 4 5 6 1 3