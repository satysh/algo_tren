nums = set(map(int, input().split()))
N = int(input())

dim = 5
div = 10000
while N // div == 0:
    dim -= 1
    div //= 10

to_display = set()
for _ in range(dim, 1, -1):
    curr = N // div
    to_display.add(curr)
    N -= curr * div
    div //= 10
to_display.add(N)

to_display -= nums
print(len(to_display))

