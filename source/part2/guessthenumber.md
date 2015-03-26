# Guess the number

![](/images/part2_guessthenumber1.png)

## beta1 2015/03/26/13:46

由于时间紧张，我采取的策略是先找出已完成学员的代码，看懂他们的写法，在综合几个代码的优点，写出我的代码。

当然目前还是不够满意。晚上再更新一个版本，解决以下问题：

- 把文字加入画布
- 增加对输入非整型的判断
- 增加自主选择猜数字范围的选项

以下是我的代码
---
# This is "Guess the number"

import random
import simplegui
import math

# 建立框架和画布
message = "Guess the number"
frame = simplegui.create_frame("Guess the number", 400, 180, 100)

def draw(canvas):
    canvas.draw_text(message, [30,105], 40, "Orange")

# 定义 range1 在 0-100 内随机选择一个数字
# g-电脑给定一个随机数；
# t-次数；
# r-判定范围的逻辑值；

def range1():
    global g, t, r
    g = random.randrange(0, 100)
    t = 7
    r = 0
    print("\n请选择一个 0-100 的数字。\n你有 " + str(t) + " 次机会。\n")
    
# 定义 range2 在 0-1000 内随机选择一个数字

def range2():
    global g, t, r
    g = random.randrange(0, 1000)
    t = 10  
    r = 1
    print("\n请选择一个 0-1000 的数字。\n你有 " + str(t) + " 次机会。\n")


# helper function to start and restart the game
def new_game(guess):
    global g, t
    t = t-1
    if  r == 0  and (int(guess)<0 or int(guess)>100 or int(guess) == False):
          print("请输入 0-100 间内整数！\n")
    elif r == 1 and (int(guess)<0 or int(guess)>1000):
        print("请输入 0-1000 间内整数！\n")
    else:
        print("\n答案是"+ str(guess) +"吗？？\n")
        if int(guess) == g or t!= 0 :
            if int(guess) == g:
                print("猜中了！\n ")   
                if r == 0:
                     range1()
                elif r == 1:
                     range2()
            elif int(guess) < g:
                print("低了！\n还剩 " + str(t) + " 次机会.\n")
            elif int(guess) > g:
                print("高了！\n还剩 " + str(t) + " 次机会.\n")
        else:
            print("对不起！没猜中！\n答案是" + str(g) + "。\n要不再玩一次吧！？\n")
            if r == 0:
                     frame.start()
                     range1()
            elif r == 1:
                     frame.start()
                     range2()

# register event handlers for control elements
frame.add_button("0-100", range1, 80)
frame.add_button("0-1000", range2, 80)
frame.add_input("\n请输入数字:\n", new_game, 40)
frame.set_draw_handler(draw)


# start frame
frame.start()
print("开始游戏！\n请选择猜数字的范围！")