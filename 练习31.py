#31. 请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母.

letter = input("Please input:")
if letter == 'S':
	print("Please input the second letter")
	letter = input("Please input:")
	if letter == 'a':
		print('Saturday')
	elif letter == 'u':
		print('Sunday')
	else:
		print('Data error')

elif letter == "F":
	print('Friday')
elif letter == "M":
	print('Monday')
elif letter == 'T':
	print('Please input the second letter')
	letter = input('Please input:')
	if letter == 'u':
		print('Tuesday')
	elif letter == 'h':
		print('Thurday')
	else:
		print('Data error')