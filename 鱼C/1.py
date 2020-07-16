import random
secret = random.randint(1,10)
print('-----------------------------------------------')
temp = input("请猜一个数字：")
guess  = int(temp)
while guess != secret:
    temp = int(input("错误，请重新输入："))
    guess = int(temp)
    if guess == secret:
        print("正确！")
    else:
        if guess > secret:
            print("大了")
        else:
            print("小了")
print("游戏结束！") 
