# 杨辉三角形

n = 9

def k(i,j):
	if i==j or j==1:
		return(1)
	else:
		return(k(i-1,j-1)+k(i-1,j))
for i in range (1,n+1):
	for k1 in range(1, (n-i)*2):
		print (" ",end = "");
	for j in range (1,i+1):
		print ("%3d"%k(i,j),end = " ");
	print()

