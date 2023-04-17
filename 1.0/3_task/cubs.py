N, M = map(int, input().split())

common_set = set()
anya_set = set()
borya_set = set()

for _ in range(N):
    anya_set.add(int(input()))

for _ in range(M):
    borya_set.add(int(input()))

common_set = anya_set & borya_set
anya_set -= common_set
borya_set -= common_set

print(len(common_set))
print(*sorted(common_set))
print(len(anya_set))
print(*sorted(anya_set))
print(len(borya_set))
print(*sorted(borya_set))
