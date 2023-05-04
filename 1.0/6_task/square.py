def rcheck(d, params):
	n, m, t = params
	return (n * m - (m - 2 * d) * (n - 2 * d)) <= t

def rbinsearch(l, r, check, checkparams):
	while l < r:
		m = (l + r + 1) // 2
		if check(m, checkparams):
			l = m
		else:
			r = m - 1
	return r

n = int(input())
m = int(input())
t = int(input())

print(rbinsearch(0, min(n, m) // 2, rcheck, (n, m, t)))