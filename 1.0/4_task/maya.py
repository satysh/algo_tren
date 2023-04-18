def pack(seq):
	sym_dict = {}
	for sym in seq:
		sym_dict[sym] = sym_dict.get(sym, 0) + 1

	word = []
	for key, val in sorted(sym_dict.items()):
		word.append(key)
		word.append(str(val))

	return "".join(word)

g, S = map(int, input().split())

word_dict = {}
word = pack(input())

seq = input()

count = 0
i = 0
j = g
while True:
	if word == pack(seq[i:j]):
		count += 1
	i += 1
	j += 1

	if j > S:
		break

print(count)



