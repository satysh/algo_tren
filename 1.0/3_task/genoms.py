a = input()
b = input()

a_list = [i for i in a]
b_list = [i for i in b]


b_set = set()
for i in range(len(b) - 1):
    b_set.add(b_list[i] + b_list[i + 1])

counter = 0
for i in range(len(a_list) - 1):
    if (a_list[i] + a_list[i + 1]) in b_set:
        counter += 1

print(counter)
