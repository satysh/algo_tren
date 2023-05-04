def rcheck(d, params):
	K, L = params
	s = 0
	for l in L:
		s += l // d
	return s >= K

def rbinsearch(l, r, check, checkparams):
	while l < r:
		m = (l + r + 1) // 2
		if check(m, checkparams):
			l = m
		else:
			r = m - 1
	return r

N, K = map(int, input().split())

L = []
for _ in range(N):
	L.append(int(input()))

ans = 0
if sum(L) >= K:
	ans = rbinsearch(1, max(L), rcheck, (K, L))

print(ans)
