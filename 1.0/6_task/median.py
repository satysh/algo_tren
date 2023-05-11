def get_median(seq1, seq2, l):
    i = j = 0
    ans = 0
    while (i + j) != l:
        if i < len(seq1) and seq1[i] <= seq2[j]:
            ans = seq1[i]
            i += 1
        elif j < len(seq2) and seq2[j] < seq1[i]:
            ans = seq2[j]
            j += 1
        elif i == len(seq1):
            ans = seq2[j]
            j += 1
        elif j == len(seq2):
            ans = seq1[i]
            i += 1
    return ans

n, l = map(int, input().split())

lists = []
for _ in range(n):
    lists.append(list(map(int, input().split())))

for i in range(n - 1):
    for j in range(i + 1, n):
        print(get_median(lists[i], lists[j], l))



