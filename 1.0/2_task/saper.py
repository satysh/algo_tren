N, M, K = map(int, input().split())

field = []

for i in range(N + 2):
    field.append([])
    for _ in range(M + 2):
        field[i].append(0)

for _ in range(K):
    p, q = map(int, input().split())
    field[p][q] = "*"

neibi = [1, 1, 1, 0, 0, -1, -1, -1]
neibj = [-1, 0, 1, -1, 1, -1, 0, 1]
for i in range(1, N + 1):
    for j in range(1, M + 1):
        if field[i][j] != "*":
            count = 0
            for neib in range(8):
                if field[i + neibi[neib]][j + neibj[neib]] == "*":
                    count += 1
            '''
            if field[i - 1][j - 1] == "*":
                count += 1
            if field[i - 1][j] == "*":
                count += 1
            if field[i - 1][j + 1] == "*":
                count += 1
            if field[i][j - 1] == "*":
                count += 1
            if field[i][j + 1] == "*":
                count += 1
            if field[i + 1][j - 1] == "*":
                count += 1
            if field[i + 1][j] == "*":
                count += 1
            if field[i + 1][j + 1] == "*":
                count += 1
            '''
            field[i][j] = count

for i in range(1, N + 1):
    for j in range(1, M + 1):
        print(field[i][j], end=" ")
    print()
