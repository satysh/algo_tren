def lcheck(index, params):
	seq, x = params
	return seq[index] >= x

def lbinsearch(l, r, ckeck, checkparams):
	while l < r:
		m = (l + r) // 2
		if ckeck(m, checkparams):
			r = m
		else:
			l = m + 1
	return l

def rcheck(index, params):
	seq, x = params
	return seq[index] <= x

def rbinsearch(l, r, check, checkparams):
	while l < r:
		m = (l + r + 1) // 2
		if check(m, checkparams):
			l = m
		else:
			r = m - 1
	return r

n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

for x in b:
	rnei = rbinsearch(0, len(a) - 1, rcheck, (a, x))
	lnei = lbinsearch(0, len(a) - 1, lcheck, (a, x))

	if abs(a[rnei] - x) <= abs(a[lnei] - x):
		print(a[rnei])
	else:
		print(a[lnei])
