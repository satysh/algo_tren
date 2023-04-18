file = open("input.txt")

data_base = {}
for line in file.readlines():
    operations = list(map(str, line.split()))
    op_type = operations[0]
    name = operations[1]

    if len(operations) == 3:
        su_m = int(operations[2])
    elif len(operations) == 4:
        name1 = operations[2]
        su_m = int(operations[3])

    if op_type == "DEPOSIT":
        data_base[name] = data_base.get(name, 0) + su_m
    elif op_type == "WITHDRAW":
        data_base[name] = data_base.get(name, 0) - su_m
    elif op_type == "BALANCE":
        if name in data_base:
            print(data_base[name])
        else:
            print("ERROR")
    elif op_type == "TRANSFER":
        data_base[name] = data_base.get(name, 0) - su_m
        data_base[name1] = data_base.get(name1, 0) + su_m
    elif op_type == "INCOME":
        p = float(operations[1])
        for n_m in data_base.keys():
            curr_sum = data_base[n_m]
            if curr_sum > 0:
                curr_sum += int(curr_sum * (p / 100.))
                data_base[n_m] = curr_sum

