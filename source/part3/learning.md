#  制作可回放的点彩画板

## 编程思路

根据本次程序的预期目标，可将其拆分为五组一一对应的关系：

可视元素|图案函数|python 写法
-:-|-:-|-:-
画板|坐标|mouse button click:frame.set_mouseclick_handler()
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
WIDTH = 450  #画板宽度
HEIGHT = 300
ball_pos = [WIDTH / 2, HEIGHT / 2]
BALL_RADIUS = 15
ball_color = "Red"

# helper function
def distance(p, q):
    return math.sqrt( (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

# define event handler for mouse click, draw
def click(pos):
    global ball_pos, ball_color
    if distance(pos, ball_pos) < BALL_RADIUS:
        ball_color = "Green"
    else:
        ball_pos = list(pos)
        ball_color = "Red"

def draw(canvas):
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "Black", ball_color)

# create frame
frame = simplegui.create_frame("Mouse selection", WIDTH, HEIGHT)
frame.set_canvas_background("White")

# register event handler
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)

# start frame
frame.start()
```

