def lcheck(d, params):
	h, r, c = params

	count = 0
	i = 0
	j = c - 1
	while j < len(h):
		if (h[j] - h[i]) <= d:
			count += 1
			i += c
			j+= c
		else:
			i += 1
			j += 1

	return count >= r

def lbinsearch(l, r, ckeck, checkparams):
	while l < r:
		m = (l + r) // 2
		if ckeck(m, checkparams):
			r = m
		else:
			l = m + 1
	return l

n, r, c = map(int, input().split())

h = []
for _ in range(n):
	h.append(int(input()))

h.sort()
print(lbinsearch(0, h[-1] - h[0], lcheck, (h, r, c)))
