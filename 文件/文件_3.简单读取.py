file_name = 'demo2.txt'

try:
	# 调用open()来打开一个文件，可以将文件分层两种类型
	# 一种，是纯文本文件（使用utf-8等编码编写的文本文件）
	# 一种，是二进制文件（图片、mp3、ppt等文件）
	# open()打开文件时，默认是以文本文件的形式打开的，但是open()默认的编码为None
	# 所以处理文本文件时，必须要指定的文件编码
	with open(file_name,encoding='utf-8') as file_obj:
		# 通过 read() 来读取文件中的内容
		# 如果直接调用read()它会将文本文件的所有内容全部读取出来
		# 如果要读取的文件较大的话，会一次性将文件的内容加载到内存中，容易导致内存泄漏
		# 所以对于较大的文件，不要直接调用read()
		#help(file_obj.read)
		#read()可以接受一个size作为参数，该参数用来指定要读取的字符数量
		# 默认值为-1,它会读取文件中的所有字符
		# 可以为size指定一个值，这样read()会读取指定数量的字符，
		#	每一次读取都是从上次读取到位置开始读取的
		# 	如果字符的数量小于size，则会读取剩余所有的
		# 	如果已经读取到了文件的最后了，则会返回''空串
		# content = file_obj.read(-1)
		content = file_obj.read(6)
		content = file_obj.read(6)
		content = file_obj.read(6)
		content = file_obj.read(6)
		print(content)
		print(len(content))
except FileNotFoundError:
	print(f'(file_name)文件不存在！')