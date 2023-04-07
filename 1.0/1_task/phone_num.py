def format(num):
	if "-" in num:
		num = "".join(num.split("-"))
	if "(" in num:
		num = "".join(num.split("("))
	if ")" in num:
		num = "".join(num.split(")"))
	if "+" in num:
		num = "8" + num[2:]

	if len(num) < 11:
		num = "8495" + num
	return num

def print_t(numi, num1):
	if numi == num1:
		print("YES")
	else:
		print("NO")
num1 = format(input())
num2 = format(input())
num3 = format(input())
num4 = format(input())

print_t(num2, num1)
print_t(num3, num1)
print_t(num4, num1)