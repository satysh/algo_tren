def lcheck(a, params):
	w, h, n = params
	return (a // w) * (a // h) >= n

def lbinsearch(l, r, ckeck, checkparams):
	while l < r:
		m = (l + r) // 2
		if ckeck(m, checkparams):
			r = m
		else:
			l = m + 1
	return l

w, h, n = map(int, input().split())
print(lbinsearch(0, max(w, h) * n, lcheck, (w, h, n)))