#37. 对10个数进行排序。

print ('请输入10个数字:\n')
a=[]
for n in range(10):
    a.append(int(input('输入一个数字:\n')))
a.sort()
print (a)