#6. 斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。

def f(n):
	a,b = 1,1
	for i in range(n-1):
		a,b = b,a+b
		print(a)
	return a
f(100)