def get_ans(a, b, n, m):
    if a > b:
        return get_ans(b, a, m, n)

    amin_time = (a + 1) * n - a
    amax_time = (a + 1) * n + a
    bmin_time = (b + 1) * m - b
    bmax_time = (b + 1) * m + b

    if amax_time < bmin_time:
        return [-1]

    min_time = float('inf')
    max_time = 0

    for i in range(amin_time, amax_time + 1):
        for j in range(bmin_time, bmax_time + 1):
            if i == j:
                if min_time > i:
                    min_time = i
                if max_time < i:
                    max_time = i

    if min_time == float('inf') or max_time == 0:
        return [-1]

    return [min_time, max_time]


def main():
    a = int(input())
    b = int(input())
    n = int(input())
    m = int(input())

    print(*get_ans(a, b, n, m))


if __name__ == '__main__':
    main()
