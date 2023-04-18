file = open("input.txt")

data_base = {}

for line in file.readlines():
    buyer, product, cnt = map(str, line.split())
    cnt = int(cnt)
    if buyer not in data_base:
        data_base[buyer] = {}
        data_base[buyer][product] = cnt
    else:
        data_base[buyer][product] = data_base[buyer].get(product, 0) + cnt

for buyer, products in sorted(data_base.items()):
    print(buyer + ":")
    for product, cnt in sorted(products.items()):
        print(product, cnt)

