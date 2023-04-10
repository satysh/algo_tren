a, b, c, d = map(int, input().split())
if a > b:
    a, b = b, a
if c > d:
    c, d = d, c

smin = a * b * c * d
x = y = 0

if (a + c) * max(b, d) < smin:
    smin = (a + c) * max(b, d)
    x = a + c
    y = max(b, d)
if (a + d) * max(b, c) < smin:
    smin = (a + d) * max(b, c)
    x = a + d
    y = max(b, c)
if (b + c) * max(a, d) < smin:
    smin = (b + c) * max(a, d)
    x = b + c
    y = max(a, d)
if (b + d) * max(a, c) < smin:
    x = b + d
    y = max(a, c)

print(x, y)
