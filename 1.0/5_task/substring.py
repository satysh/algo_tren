n, k = map(int, input().split())
s = input()

cntdict = {}
mempos = 0
maxlen = 0

r = 0
cntdict[s[r]] = 1
for l in range(n):

	while r < n and cntdict[s[r]] <= k:
		r += 1
		if r == n:
			break
		cntdict[s[r]] = cntdict.get(s[r], 0) + 1


	if maxlen < (r - l):
		mempos = l
		maxlen = r - l

	cntdict[s[l]] -= 1

print(maxlen, mempos + 1)
