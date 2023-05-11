def lcheck(index, params):
    median, seq = params
    return seq[index] > median

def lbinsearch(l, r, ckeck, checkparams):
    while l < r:
        m = (l + r) // 2
        if ckeck(m, checkparams):
            r = m
        else:
            l = m + 1
    return l

def get_median(seq1, seq2, l):
    left = min(seq1[0], seq2[0])
    right = max(seq1[-1], seq2[-1])

    while left < right:
        median = (left + right) // 2
        nelemleft = lbinsearch(0, len(seq1) - 1, lcheck, (median, seq1))
        if nelemleft == len(seq1) - 1:
            if seq1[-1] <= median:
                nelemleft += 1
        nelemright = lbinsearch(0, len(seq2) - 1, lcheck, (median, seq2))
        if nelemright == len(seq2) - 1:
            if seq2[-1] <= median:
                nelemright += 1
        nelemleft += nelemright
        if nelemleft == 0:
            return min(seq1[0], seq2[0])
        if nelemleft >= l:
            right = median
        else:
            left = median + 1
    return left

n, l = map(int, input().split())

lists = []
for _ in range(n):
    x, d, a, c, m = map(int, input().split())
    nowlist = [x]
    for _ in range(1, l):
        x = x + d
        nowlist.append(x)
        d = ((a * d + c) % m)
    lists.append(nowlist)

for i in range(n - 1):
    for j in range(i + 1, n):
        print(get_median(lists[i], lists[j], l))
