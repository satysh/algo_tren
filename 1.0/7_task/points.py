n, m = map(int, input().split())

events = []
for _ in range(n):
	a, b = map(int, input().split())
	if a > b:
		a, b = b, a
	events.append((a, -1))
	events.append((b, 1))

events.sort()

points = list(map(int, input().split()))
points_dict = {point:0 for point in points}
points_keys = set(points_dict)
points_keys = sorted(points_keys)


accum = 0
i = 0
for event in events:
	if event[1] == -1:
		while i < len(points_keys) and points_dict[points_keys[i]] == 0 and event[0] > points_keys[i]:
			points_dict[points_keys[i]] = accum
			i += 1 
		accum += 1
	else:
		while i < len(points_keys) and points_dict[points_keys[i]] == 0 and event[0] >= points_keys[i]:
			points_dict[points_keys[i]] = accum
			i += 1
		accum -= 1

for point in points:
	print(points_dict[point], end=' ')
print()

