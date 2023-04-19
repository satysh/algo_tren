def form_sub_seq(seq):
	sub_seq = [0] * 52
	for sym in seq:
		code = ord(sym)
		if code >= 65 and code <= 90:
			sub_seq[code - 65] += 1
		elif code >= 97 and code <= 122:
			sub_seq[code - 71] += 1

	return sub_seq

def isequal(seq1, seq2):
	for i in range(52):
		if seq1[i] != seq2[i]:
			return False
	return True

def update_seq(seq, sym_to_del, sym_to_add):
	code_to_del = ord(sym_to_del)
	code_to_add = ord(sym_to_add)

	if code_to_del >= 65 and code_to_del <= 90:
		seq[code_to_del - 65] -= 1
	elif code_to_del >= 97 and code_to_del <= 122:
		seq[code_to_del - 71] -= 1

	if code_to_add >= 65 and code_to_add <= 90:
		seq[code_to_add - 65] += 1
	elif code_to_add >= 97 and code_to_add <= 122:
		seq[code_to_add - 71] += 1

g, S = map(int, input().split())

word_dict = {}
word = form_sub_seq(input())

seq = input()

count = 0
i = 0
j = g - 1
sub_seq = form_sub_seq(seq[i:j + 1])
while True:
	if isequal(word, sub_seq):
		count += 1
	j += 1
	if j >= S:
		break
	update_seq(sub_seq, seq[i], seq[j])
	i += 1

print(count)



