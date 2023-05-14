n, m = map(int, input().split())

events = []
for _ in range(m):
	beg, end = map(int, input().split())
	events.append((beg, -1))
	events.append((end, 1))

events.sort()

counter = events[0][0]
sauron = 0
flag = False
mem = 0
for event in events:
	if event[1] == -1:
		sauron += 1
	else:
		sauron -= 1

	if sauron == 0:
		flag = True
		mem = event[0] + 1
	elif flag:
		counter += event[0] - mem
		flag = False

counter += n - mem
print(counter)


