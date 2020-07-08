#8. 输出 9*9 乘法口诀表。

for i in range(1,10):
	for j in range(1,i+1):
		print ("%d*%d=%d%s"%(i,j,i*j,  ' 'if i*j<10 and j>1 else''),end = " ")
	print()
