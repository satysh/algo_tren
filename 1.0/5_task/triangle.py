n = int(input())

points = []
for _ in range(n):
    xi, yi = map(int, input().split())
    points.append((xi, yi))

ans = 0
for i in range(n):
    antidegeneration = set()

    neigs = []
    for j in range(n):
        xvect = points[i][0] - points[j][0]
        yvect = points[i][1] - points[j][1]

        vect = xvect ** 2 + yvect ** 2

        neigs.append(vect)

        if (xvect, yvect) in antidegeneration:
            ans -= 1

        antidegeneration.add((-xvect, -yvect))

    neigs.sort()

    r = 0
    for l in range(len(neigs)):
        while r < len(neigs) and neigs[l] == neigs[r]:
            r += 1
        ans += r - l - 1

print(ans)
