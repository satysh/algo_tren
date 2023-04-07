a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

if d > e:
	d, e = e, d
if a > b:
	a, b = b, a
if b > c:
	b, c = c, b
if a > b:
	a, b = b, a

if a <= d and b <= e:
	print("YES")
else:
	print("NO")