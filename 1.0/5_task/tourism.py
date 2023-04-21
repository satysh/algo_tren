def get_prefix_sum(peaks):
    prefix_sum = [0] * len(peaks)
    for i in range(1, N):
        _prev_xi, prev_yi = peaks[i - 1]
        _curr_xi, curr_yi = peaks[i]
        diff = curr_yi - prev_yi
        diff = diff if diff > 0 else 0
        prefix_sum[i] = prefix_sum[i - 1] + diff

    return prefix_sum

N = int(input())

peaks = []

for _ in range(N):
    xi, yi = map(int, input().split())
    peaks.append((xi, yi))

prefix_sum_lr = get_prefix_sum(peaks)
prefix_sum_rl = get_prefix_sum(peaks[::-1])[::-1]

M = int(input())

for _ in range(M):
    L, R = map(int, input().split())
    ans = 0
    if L > R:
        print(prefix_sum_rl[R - 1] - prefix_sum_rl[L - 1])
    else:
        print(prefix_sum_lr[R - 1] - prefix_sum_lr[L - 1])

# 2
# 7 12
# 9 19
# 10
# 2 1
# 2 1
# 2 1
# 2 2
# 2 1
# 1 1
# 2 2
# 1 2
# 1 1
# 1 2
