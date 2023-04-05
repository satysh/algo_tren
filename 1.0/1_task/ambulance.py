import math

def main():
    K1, M, K2, P2, N2 = map(int, input().split())

    P1 = N1 = 0
    if N2 > K2 or N2 > M or P2 > K2:
        P1 = N1 = -1
    elif (N2 == K2) and P2 != 1:
        P1 = N1 = -1
    elif (P2 == K2) and M != 1:
        P1 = N1 = -1
    elif K2 == 1:
        P1 = 0
        N1 = 1
    elif P2 == N2 == 1:
        if M == 1:
            P1 = 0
            N1 = 1
        elif K1 <= K2 * M:
            P1 = 1
            N1 = 0
        else:
            P1 = N1 = 0
    else:
        n = math.ceil(K2 / ((P2 - 1) * M + N2))
        P1 = math.ceil(K1 / (M * n))
        N1 = math.ceil((K1 / n - (P1 - 1) * M))

    print(P1, N1)
if __name__ == '__main__':
    main()
