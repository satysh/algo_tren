
def main():
	a = int(input())
	b = int(input())
	c = int(input())

	if c < 0:
		print("NO SOLUTION")
	elif a == 0:
		if (b < 0 or b != c * c):
			print("NO SOLUTION")
		else:
			print("MANY SOLUTIONS")
	elif a == b == c == 0:
		print("MANY SOLUTIONS")
	else:
		x = (c * c - b)
		if x % a == 0:
			print(int(x / a))
		else:
			print("NO SOLUTION")


if __name__ == '__main__':
	main()