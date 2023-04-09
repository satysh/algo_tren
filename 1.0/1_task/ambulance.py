import math

def get_apperfloor_min_and_max(K2, f2):
    apperfloor_min = math.ceil((K2 - 1) / f2)
    if apperfloor_min * f2 < K2:
        apperfloor_min = math.ceil(K2 / f2)
    itK2 = K2
    while (itK2 - 1) % (f2 - 1) != 0:
        itK2 -= 1
    apperfloor_max = int((itK2 - 1) / (f2 - 1))

    return apperfloor_min, apperfloor_max

def get_ans(K1, M, K2, P2, N2):
    f2 = N2 + M * (P2 - 1) # new floor number 
    P1 = N1 = 0
    if N2 > K2 or N2 > M or P2 > K2 or f2 > K2:
        P1 = N1 = -1
    elif K2 == 1:
        if M == 1:
            N1 = 1
    elif f2 == 1:
        if K1 <= K2 * M:
            P1 = 1
        if K1 <= K2:
            N1 = 1
    else:
        apperfloor_min, apperfloor_max = get_apperfloor_min_and_max(K2, f2)
        if apperfloor_min > apperfloor_max:
            return -1, -1

        flagP1 = False
        flagN1 = False
        while K1 % apperfloor_min != 0:
            K1 += 1
        f1 = int(K1 / apperfloor_min)
        P1 = math.ceil(f1 / M)
        N1 = f1 - M * (P1 - 1)
        for apperfloor in range(apperfloor_min + 1, apperfloor_max + 1):
            while K1 % apperfloor != 0:
                K1 += 1
            f1 = int(K1 / apperfloor)
            nextP1 = math.ceil(f1 / M)
            nextN1 = f1 - M * (nextP1 - 1)

            if nextP1 != P1:
                flagP1 = True
            if nextN1 != N1:
                flagN1 = True

        if flagP1:
            P1 = 0
        if flagN1:
            N1 = 0

    return P1, N1


def main():
    K1, M, K2, P2, N2 = map(int, input().split())
    print(*get_ans(K1, M, K2, P2, N2))
     
if __name__ == '__main__':
    main()
