#36. 求100之内的素数。

lower = int(input("最小值："))
upper = int(input("最大值："))

for num in range(lower,upper+1):
	if num > 1:
		for i in range(2,num):
			if(num % i) == 0:
				break
		else:
			print(num)  