def lcheck(t, params):
	N, x, y = params
	return (t // x + t // y) >= N

def lbinsearch(l, r, ckeck, checkparams):
	while l < r:
		m = (l + r) // 2
		if ckeck(m, checkparams):
			r = m
		else:
			l = m + 1
	return l

N, x, y = map(int, input().split())
print(lbinsearch(0, N * max(x, y), lcheck, (N - 1, x, y)) + min(x, y))