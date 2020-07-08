#14. 将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。

while True:
    n = int(input("请输入一个正整数："))
    print ("%d = " %n , end = '')
    while n not in [1]:
        for i in range(2, n+1):
            if n % i == 0:
                n = int(n/i)
                if n == 1:
                    print("%d " %i , end = '')
                else:
                    print("%d * " %i , end = '')
                break
    print()