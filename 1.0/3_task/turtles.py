N = int(input())

honest_turtles = set()
for _ in range(N):
    ai, bi = map(int, input().split())
    if ai >= 0 and bi >=0:
        if (ai + bi + 1) == N:
            if (N - bi) not in honest_turtles:
                honest_turtles.add(N - bi)

print(len(honest_turtles))
