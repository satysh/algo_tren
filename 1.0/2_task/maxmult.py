def forma_t(x, y):
	if x <= y:
		print(x, y)
	else:
		forma_t(y, x)

a = list(map(int, input().split()))

max_positive = max(a[0], a[1])
max_positive2 = min(a[0], a[1])


for i in range(2, len(a)):
	if a[i] > max_positive:
		max_positive, max_positive2 = a[i], max_positive
	elif a[i] > max_positive2:
		max_positive2 = a[i]

max_negative = 0
max_negative2 = 1

for i in range(len(a)):
	if a[i] < 0:
		if max_negative == 0:
			max_negative = a[i]
		else:
			if a[i] < max_negative:
				max_negative, max_negative2 = a[i], max_negative
			elif a[i] < max_negative2:
				max_negative2 = a[i]


if max_positive * max_positive2 >= max_negative * max_negative2:
	forma_t(max_positive, max_positive2)
else:
	forma_t(max_negative, max_negative2)
