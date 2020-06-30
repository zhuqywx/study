#36. 求100之内的素数。

lower = int(input("输入区间最小值："))
upper = int(input("输入区间最大值："))

for i in range(lower,upper + 1):
	if i > 1:
		for j in range(2,i):
			if(i % j) == 0:
				break
		else:
			print(i)

