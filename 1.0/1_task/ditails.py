N, K, M = map(int, input().split())

c = 0
# 30 5 7 
k = N // K
while k > 0 and K >= M:
	N -= k * K
	m = k * (K // M)
	c += m
	N += k * K - m * M
	k = N // K

print(c)
