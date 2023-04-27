def checker(m, params):
	a, x = params
	return a[m] >= x


def left_bins(l, r, check, params):
	while l < r:	
		m = (l + r) // 2
		if check(m, params):
			r = m
		else:
			l = m + 1

	return l


def main():
	n, k = map(int, input().split())
	a = list(map(int, input().split()))
	b = list(map(int, input().split()))

	for x in b:
		ai = left_bins(0, n - 1, checker, (a, x))
		if a[ai] == x:
			print("YES")
		else:
			print("NO")


if __name__ == '__main__':
	main()