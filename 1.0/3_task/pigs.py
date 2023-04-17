N = int(input())

shots = set()
for _ in range(N):
    x, _y = map(int, input().split())
    shots.add(x)

print(len(shots))

