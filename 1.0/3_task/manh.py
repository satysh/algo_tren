def extend(points, t):
    minPosX, maxPosX, minPosY, maxPosY = points
    return (minPosX - t, maxPosX + t, minPosY - t, maxPosY + t)

def intersect(points1, points2):
    minPosX1, maxPosX1, minPosY1, maxPosY1 = points1
    minPosX2, maxPosX2, minPosY2, maxPosY2 = points2
    return (max(minPosX1, minPosX2), min(maxPosX1, maxPosX2), max(minPosY1, minPosY2), min(maxPosY1, maxPosY2))

t, d, n = map(int, input().split())

misha_points = (0, 0, 0, 0)
for _ in range(n):
    misha_points = extend(misha_points, t)
    xi, yi = map(int, input().split())
    navig_points = extend((xi - yi, xi - yi, xi + yi, xi + yi), d)
    misha_points = intersect(misha_points, navig_points)

ans = []
for xminusY in range(misha_points[0], misha_points[1] + 1):
    for xplusY in range(misha_points[2], misha_points[3] + 1):
        if (xminusY + xplusY) % 2 == 0:
            x = (xminusY + xplusY) // 2
            y = xplusY - x
            ans.append((x, y))

print(len(ans))
for point in ans:
    print(*point)


