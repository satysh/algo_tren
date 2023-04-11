prev_num = float(input())
curr_num = float(input())

types = set()
if curr_num == -2 * 10**9:
    types.add("CONSTANT")

while curr_num != -2 * 10**9:
    if prev_num == curr_num:
        types.add("CONSTANT")
    elif prev_num < curr_num:
        types.add("ASCENDING")
    elif prev_num > curr_num:
        types.add("DESCENDING")
    prev_num, curr_num = curr_num, float(input())

if len(types) == 1:
    print(*types)
elif len(types) == 2 and "CONSTANT" in types:
    types.discard("CONSTANT")
    print("WEAKLY", *types)
else:
    print("RANDOM")

