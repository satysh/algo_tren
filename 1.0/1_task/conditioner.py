troom, tcond = map(int, input().split())
mode = input()

tresult = 0
if mode == "fan":
	tresult = troom
elif mode == "auto":
	tresult = tcond
elif mode == "heat":
	tresult = tcond if troom < tcond else troom
elif mode == "freeze":
	tresult = tcond if troom > tcond else troom

print(tresult)

