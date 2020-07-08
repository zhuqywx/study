#10. 暂停一秒输出，并格式化当前时间。

import time,datetime

time.sleep(1)
TIME1 = datetime.datetime.now()
print(TIME1.strftime("%Y.%m.%d %H:%M:%S"))
time.sleep(1)
TIME2 = datetime.datetime.now()
print(TIME2.strftime("%Y.%m.%d %H:%M:%S"))