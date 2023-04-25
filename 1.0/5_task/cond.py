n = int(input())
a = list(map(int, input().split()))

m = int(input())
c_b = []

for _ in range(m):
	b, c = map(int, input().split())
	c_b.append((c, b))

a.sort()
c_b.sort()


min_sum = 0
j = 0
for ai in a:
	while j < len(c_b):
		if ai <= c_b[j][1]:
			min_sum += c_b[j][0]
			break
		j += 1

print(min_sum)
















'''
n = int(input())
a = list(map(int, input().split()))

m = int(input())
c_b = []

for _ in range(m):
	b, c = map(int, input().split())
	c_b.append((c, b))

a.sort()
c_b.sort()

min_sum = 0

for ai in a:
	for c_bj in c_b:
		if c_bj[1] >= ai:
			min_sum += c_bj[0]
			break

print(min_sum)
'''
