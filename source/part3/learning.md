#  制作可回放的点彩画板

## 编程思路

根据本次程序的预期目标，可将其拆分为五组一一对应的关系：

可视元素|图案函数|python 写法
----|----|----
画板|坐标|frame.set_mouseclick_handler()
圆形按钮、方形按钮、三角形按钮|形状
色板按钮|颜色
回放按钮|时序
加速按钮、减速按钮|间隔

## 代码学习

### 1. mouse_input

- [示例代码](http://www.codeskulptor.org/#examples-mouse_input.py)

```python
# Examples of mouse input

import simplegui
import math

# intialize globals
WIDTH = 450   #定义变量 WIDTH，初始值为 450
HEIGHT = 300  #定义变量 HEIGHT，初始值为 450
ball_pos = [WIDTH / 2, HEIGHT / 2]  #定义含有两个数字的列表变量 ball_pos，且数字分布为二分之一 WIDTH 和二分之一 HEIGHT（调用为坐标，即为画布中心）
BALL_RADIUS = 15  #定义变量 BALL_RADIUS，初始值为15（后面调用为圆点的半径）
ball_color = "Red"  #定义变量 ball_color，初始值为 "Red"（后面调用为圆点的颜色）

# helper function
    return math.sqrt( (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

# define event handler for mouse click, draw
def click(pos):  #定义事件click
    global ball_pos, ball_color
    if distance(pos, ball_pos) < BALL_RADIUS:
        ball_color = "Green"
    else:
        ball_pos = list(pos)
        ball_color = "Red"

def draw(canvas):
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "Black", ball_color)

# create frame
frame = simplegui.create_frame("Mouse selection", WIDTH, HEIGHT)  #以 WIDTH, HEIGHT 初始值为宽度和高度创建画框
frame.set_canvas_background("White")  #设置画布颜色为白色

# register event handler
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)

# start frame
frame.start()
```

