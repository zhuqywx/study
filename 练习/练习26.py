#26.利用递归方法求5!。（递归公式：fn=fn_1*4!）

i = int(input('请输入:'))
def fact(j):
    sum = 0
    if j == 0:
        sum = 1
    else:
        sum = j * fact(j - 1)
    return sum
 
print (fact(i))