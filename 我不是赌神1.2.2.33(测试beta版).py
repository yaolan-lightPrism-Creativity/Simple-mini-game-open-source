a=0
b=0
import random
while a==0:
    print("""[我不是赌神]
          【1】开始游戏
          【2】游戏市场
          【3】关于我们
          【4】退出游戏
          您的积分：""",b,"""
          游戏版本：1.2.2.33（beta）""")
    way=int(input("请输入您的操作（输入数字）："))
    if way==1:
        print("""请选择游戏模式
              [1]业余模式
              [2]专家模式
              [3]噩梦模式
              [4]不开玩不了""")
        mod=int(input("请输入您的操作（输入数字）："))
        if mod==1:
            num=random.randint(1,10)
            print("游戏开始，我生成了一个1-10的随机数")
            guess=int(input("猜测这个数是："))
            if guess==num:
                print("恭喜你猜对啦！")
                b+=1
                quit=input("任意输入以返回")
                print()
                continue
            else:
                print("不对哦！")
                quit=input("任意输入以返回")
                print()
                continue
            print()
            continue
        elif mod==2:
            num=random.randint(1,100)
            print("游戏开始，我生成了一个1-100的随机数")
            guess=int(input("猜测这个数是："))
            if guess==num:
                print("恭喜你猜对啦！")
                b+=10
                quit=input("任意输入以返回")
                print()
                continue
            else:
                print("不对哦！")
                b-=1
                quit=input("任意输入以返回")
                print()
                continue
            print()
            continue
        elif mod==3:
            num=random.randint(1,500)
            print("游戏开始，我生成了一个1-500的随机数")
            guess=int(input("猜测这个数是："))
            if guess==num:
                print("恭喜你猜对啦！")
                b+=50
                quit=input("任意输入以返回")
                print()
                continue
            else:
                print("不对哦！")
                b-=5
                quit=input("任意输入以返回")
                print()
                continue
            print()
            continue
        elif mod==4:
            num=random.randint(1,1000)
            print("游戏开始，我的赌神！我生成了一个1-1000的随机数")
            guess=int(input("猜测这个数吧！："))
            if guess==num:
                print("卧槽！太牛逼了！开了吧？！")
                b+=1000
                quit=input("任意输入以返回")
                print()
                continue
            else:
                print("不对哦！我就说你不是赌神吧！菜就多练练！")
                quit=input("任意输入以返回")
                print()
                continue
            print()
            continue
        else:
            print("前面的区域，我们以后再来探索吧！")
            input("回车以返回主页")
            print()
        print()
        continue
    elif way==2:
        print("此区域正在开发……")
    elif way==3:
        print("设置")
        print("【1】关于我们")
        print("回车 返回首页")
        print("正在开发……")
        guess=int(input("您的操作："))
        if guess==1:
            print("""     【光棱创艺工作室®（老的：慕影工作室 铭之吟工作室）】
                LightPrismCreativity studio®（old:MoRen studio MZY studio）】
                加入投稿：1421646141@qq.com
                联系我们：🐧：1421646141""")
            quit=input("任意输入返回主页")
            print()
            continue
        else:
            print()
            continue
        print()
        continue
    elif way==4:
        a+=1
        print()
        continue
    else:
        print("前面的区域，我们以后再来探索吧！")
        input("回车以返回主页")
        print()
    continue
print("""           【您已退出游戏，若想再次打开，请关闭该窗口。】
【You've quit the game, and if you want to open it again, close the window.】""")
