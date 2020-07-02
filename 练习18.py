#18.求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个）

n = int(input('n = '))
a = int(input('a = '))
sum = 0
total = 0
for i in range(n):
	sum += (10 ** i)
	total += sum * a
print(total)

