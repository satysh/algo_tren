N = int(input())
tshit_cloros = list(map(int, input().split()))

M = int(input())
trousers_colors = list(map(int, input().split()))

style = tshit_cloros[-1] + trousers_colors[-1] # inf
best_thsit_color = tshit_cloros[0]
best_trousers_color = trousers_colors[0]


i = j = 0
while i < len(tshit_cloros) and j < len(trousers_colors):
    trousers_minus_tshit = trousers_colors[j] - tshit_cloros[i]
    if trousers_minus_tshit > 0:
        if style > trousers_minus_tshit:
            style = trousers_minus_tshit
            best_thsit_color = tshit_cloros[i]
            best_trousers_color = trousers_colors[j]
        i += 1
    elif trousers_minus_tshit < 0:
        if style > abs(trousers_minus_tshit):
            style = abs(trousers_minus_tshit)
            best_thsit_color = tshit_cloros[i]
            best_trousers_color = trousers_colors[j]
        j += 1
    elif trousers_minus_tshit == 0:
        best_thsit_color = tshit_cloros[i]
        best_trousers_color = trousers_colors[j]
        break

print(best_thsit_color, best_trousers_color)

# 2
# 4 5
# 3
# 1 2 3

