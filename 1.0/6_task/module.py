def rcheck(d, params):
	n, a, b, w, h = params
	first = (w // (b + 2 * d)) * (h // (a + 2 * d))
	second = (h // (b + 2 * d)) * (w // (a + 2 * d))
	third = max(first, second)
	return third >= n

def rbinsearch(l, r, check, checkparams):
	while l < r:
		m = (l + r + 1) // 2
		if check(m, checkparams):
			l = m
		else:
			r = m - 1
	return r


n, a, b, w, h = map(int, input().split())

# а всегда меньше b
if a > b:
	a, b = b, a
# w всегда меньше h
if w > h:
	w, h = h, w

print(rbinsearch(0, h, rcheck, (n, a, b, w, h)))


