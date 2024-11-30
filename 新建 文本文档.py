a=0
b=0
import random
while a==0:
    print("""[我不是赌神]
          【1】
          【2】
          【3】
          【4】
          您的积分：""",b)
    way=int(input("请输入您的操作（输入数字）："))
    if way==1:
        print("""请选择游戏模式
              [1]
              [2]
              [3]
              [4]""")
        mod=int(input("请输入您的操作（输入数字）："))
        if mod==1:
            num=random.randint(1,10)
            print("游戏开始，我生成了一个1-10的随机数")
            guess=int(input("猜测这个数是："))
            if guess==num:
                print("恭喜你猜对啦！")
                b+=1
                quit=input("任意输入以返回")
                continue
            else:
                print("不对哦！")
                quit=input("任意输入以返回")
                continue
            continue
        elif mod==2:
            num=random.randint(1,100)
            print("游戏开始，我生成了一个1-100的随机数")
            guess=int(input("猜测这个数是："))
            if guess==num:
                print("恭喜你猜对啦！")
                b+=10
                quit=input("任意输入以返回")
                continue
            else:
                print("不对哦！")
                b-=1
                quit=input("任意输入以返回")
                continue
            continue
        elif mod==3:
            num=random.randint(1,500)
            print("游戏开始，我生成了一个1-500的随机数")
            guess=int(input("猜测这个数是："))
            if guess==num:
                print("恭喜你猜对啦！")
                b+=50
                quit=input("任意输入以返回")
                continue
            else:
                print("不对哦！")
                b-=5
                quit=input("任意输入以返回")
                continue
            continue
        elif mod==4:
            num=random.randint(1,1000)
            print("游戏开始，我的赌神！我生成了一个1-1000的随机数")
            guess=int(input("猜测这个数吧！："))
            if guess==num:
                print("卧槽！太牛逼了！开了吧？！")
                b+=1000
                quit=input("任意输入以返回")
                continue
            else:
                print("不对哦！我就说你不是赌神吧！菜就多练练！")
                quit=input("任意输入以返回")
                continue
            continue
    elif way==4:
        a+=1
        continue
    continue
print("""           您已退出游戏，若想再次打开，请关闭该窗口
You've quit the game, and if you want to open it again, close the window.""")
