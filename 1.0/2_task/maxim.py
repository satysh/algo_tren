def is_inside(val, left, right):
	if val >= left and val <= right:
		return True
	else:
		return False

n = int(input())

left = 30.
right = 4000.

curr = float(input())
for _ in range(n - 1):
	read = list(map(str, input().split()))
	curr, prev = float(read[0]), curr
	status = read[1]
	median = 0.5 * (prev + curr)

	if is_inside(median, left, right):
		if curr > prev:
			if status == "closer":
				left = median
			elif status == "further":
				right = median
		elif curr < prev:
			if status == "closer":
				right = median
			elif status == "further":
				left = median

print(left, right)


