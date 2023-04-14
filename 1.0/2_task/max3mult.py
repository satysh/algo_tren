def get_ans(a):
    ma_x1 = -float("inf")
    ma_x2 = -float("inf")
    ma_x3 = -float("inf")

    mi_n1 = float("inf")
    mi_n2 = float("inf")

    for ai in a:
        if ma_x1 < ai:
            ma_x1, ma_x2, ma_x3 = ai, ma_x1, ma_x2
        elif ma_x2 < ai:
            ma_x2, ma_x3 = ai, ma_x2
        elif ma_x3 < ai:
            ma_x3 = ai

        if ai < 0:
            if mi_n1 > ai:
                mi_n1, mi_n2 = ai, mi_n1
            elif mi_n2 > ai:
                mi_n2 = ai


    x1, x2, x3 = ma_x1, ma_x2, ma_x3

    if mi_n1 != float("inf") and mi_n2 != float("inf"):
        if mi_n1 * mi_n2 * x1 > x1 * x2 * x3:
            x2, x3 = mi_n1, mi_n2

    print(x1, x2, x3)


a = list(map(int, input().split()))

if len(a) < 3:
    print()
else:
    get_ans(a)


# 1 2 3
# -3 -2 -1 1 1 1
# 1 0 5
# -3 0 -5 -7

