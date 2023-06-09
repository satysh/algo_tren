def firts_uncompatible_index(params):
	events, i = params
	if i + 1 == len(events):
		return i + 1
	beg1, end1 = events[i]
	j = i + 1
	beg2, end2 = events[j]
	while end1 - beg2 >= 5:
		j += 1
		if j < len(events):
			beg2, end2 = events[j]
		else:
			break

	return j


def main():
	n = int(input())
	events = []
	for _ in range(n):
		begi, endi = map(int, input().split())
		if endi - begi >= 5:
			events.append((begi, endi))

	events.sort()
	try:
		ans = [1, events[0][0], events[0][1] + 1]
	except:
		ans = [0, 1, 6]

	for i in range(len(events) - 1):
		cur_uncompatible_index = firts_uncompatible_index((events, i))
		print(cur_uncompatible_index)
		cur_compatible_number = cur_uncompatible_index - i

		if cur_compatible_number > ans[0]:
				ans[0] = cur_compatible_number
				ans[1] = events[cur_uncompatible_index - 1][0]
				ans[2] = events[cur_uncompatible_index - 1][1] + 1

		for j in range(cur_uncompatible_index, len(events)):
			next_uncompatible_index = firts_uncompatible_index((events, j))
			next_compatible_number = next_uncompatible_index - j
			if cur_compatible_number + next_compatible_number > ans[0]:
				ans[0] = cur_compatible_number + next_compatible_number
				ans[1] = events[cur_uncompatible_index - 1][0]
				ans[2] = events[next_uncompatible_index - 1][0]


	print(*ans)

if __name__ == '__main__':
	main()