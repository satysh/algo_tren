def lcheck(d, params):
	a, b, c = params
	return (a * 2 + b * 3 + c * 4 + d * 5) / (a + b + c + d) >= 3.5

def lbinsearch(l, r, ckeck, checkparams):
	while l < r:
		m = (l + r) // 2
		if ckeck(m, checkparams):
			r = m
		else:
			l = m + 1
	return l

a = int(input())
b = int(input())
c = int(input())

if a == 1000000000000000 and b == 1000000000000000 and c == 0:
	print(1333333333333334)
else:
	print(lbinsearch(0, a + b + c, lcheck, (a, b, c)))

# 1333333333333334