def get_ans(dists):
    max_dists = dists[0]
    max_dists_index = 0
    for i in range(1, len(dists)):
        if max_dists < dists[i]:
            max_dists = dists[i]
            max_dists_index = i

    vasya_max_dists = 0
    for i in range(max_dists_index + 1, len(dists) - 1):
        if str(dists[i])[-1] == "5" and dists[i] > dists[i + 1] and vasya_max_dists < dists[i]:
            vasya_max_dists = dists[i]


    if vasya_max_dists == 0:
        return 0

    dists.sort(reverse=True)

    pos = 0
    for dist in dists:
        pos += 1
        if dist == vasya_max_dists:
            break

    return pos


n = int(input())
dists = list(map(int, input().split()))
print(get_ans(dists))


# 7
# 10 20 15 10 30 5 1

# 3
# 15 15 10

# 3
# 10 15 20

# 10
# 555 76 661 478 889 453 555 359 601 835
# 889 835 661 601 555 555 478 453 359 76
