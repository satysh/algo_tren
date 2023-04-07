import math

def main():
    K1, M, K2, P2, N2 = map(int, input().split())

    P1 = N1 = 0
    if N2 > K2 or N2 > M or P2 > K2:
        P1 = N1 = -1
    elif (N2 == K2) and P2 != 1:
        P1 = N1 = -1
    elif P2 != 1 and (P2 == K2) and M != 1:
        P1 = N1 = -1
    elif K1 == K2:
        P1 = P2
        N1 = N2
    elif P2 == 1:
        if M == 1:
            N1 = 1
        elif N2 == 1 and K2 == 1:
            pass
        elif N2 == 1 and K1 <= K2 * M:
            P1 = P2
            if K1 <= K2:
                N1 = N2
        else:
            min_n = math.ceil(K2 / N2)
            max_n = (K2 - 1) // (N2 - 1)
            P1 = math.ceil(K1 / (M * min_n))
            N1 = math.ceil(K1 / min_n - (P1 - 1) * M)
            flagP = flagN = False
            for i in range(min_n + 1, max_n + 1):
                P11 = math.ceil(K1 / (M * i))
                N11 = math.ceil((K1 / i - (P11 - 1) * M))
                if P1 != P11:
                    flagP = True
                if N1 != N11:
                    flagN = True
            if flagP:
                P1 = 0
            if flagN:
                N1 = 0
    else:
        n = math.ceil(K2 / ((P2 - 1) * M + N2))
        P1 = math.ceil(K1 / (M * n))
        N1 = math.ceil((K1 / n - (P1 - 1) * M))

    print(P1, N1)
if __name__ == '__main__':
    main()
