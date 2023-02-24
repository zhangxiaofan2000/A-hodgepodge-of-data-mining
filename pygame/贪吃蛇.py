# -*- coding: utf-8 -*-
# Auther : ZhangYiLong
# Mail : 503302425@qq.com
# Date : 2023/2/10 16:21
# File : 贪吃蛇.py
import pygame
import random
class Point:
    def __init__(self, row=0, col=0):
        self.row = row
        self.col = col
    def copy(self):
        return Point(self.row, self.col)
# 定义显示窗口的W(宽) H(高)
W = 800
H = 600

start_btu_W = 200
start_btu_H = 200
snakes = [] #定义蛇身列表
def ge_food():
    while True:
        pos = Point(random.randint(0, ROW - 1), random.randint(0, COL - 1))
        is_collide = False
        if pos.row == head.row and pos.col == head.col:  # 与蛇头重合
            is_collide = True
        # 与蛇身碰撞
        for snake in snakes:
            if (snake.row == pos.row and snake.col == pos.col):
                is_collide = True
                break
        if not is_collide:
            return pos
ROW = 40 #行数
COL = 30 #列数
size = (W, H)
pygame.init() # 初始化界面
window = pygame.display.set_mode(size)
pygame.display.set_caption("贪吃蛇大作战")
bak_color = (255, 255, 255)
# 定义蛇头
head = Point(row=int(ROW/2), col=int(COL/2))
head_color = (0, 128, 128)
# 定义食物
food = ge_food()
food_color = (255, 255, 0)

snake_color = (128, 128, 128)
direct = 'left'
def rect(point, color):
    cell_width = W/COL
    cell_height = H/ROW
    left = point.col*cell_width
    top = point.row*cell_height
    pygame.draw.rect(
        window, color,
        (left, top, cell_width, cell_height)
    )

showWindow = True
clock = pygame.time.Clock() #时钟控制
while showWindow:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            showWindow = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if direct=='left' or direct=='right':
                    direct = "top"
            elif event.key == pygame.K_DOWN:
                if direct == 'left' or direct == 'right':
                    direct = "down"
            elif event.key == pygame.K_LEFT:
                if direct=='top' or direct=='down':
                    direct = 'left'
            elif event.key == pygame.K_RIGHT:
                if direct == 'top' or direct == 'down':
                    direct = 'right'
    # 判断蛇是否吃到东西
    eat = False
    if head.row == food.row and head.col == food.col:# 蛇吃到食物
        eat = True
    if eat:# 吃到食物就要产生新的食物
        food = ge_food()
    # 将蛇头插入到snakes列表中
    snakes.insert(0, head.copy())
    # 将最后一个元素删除
    if not eat:
        snakes.pop()
    # 移动蛇头
    if direct == 'left':
        head.col-=1  # 注意 direct = 'left'与head.col-=1不能写在一起 因为蛇头要一直移动
    elif direct == 'right':
        head.col+=1
    elif direct == 'top':
        head.row-=1
    else:
        head.row+=1
    # 判断蛇是否死亡
    dead = False
    # 判断蛇是否撞墙
    if head.col<0 or head.row<0 or head.row>=ROW or head.col>=COL:
        dead = True
    # 判断蛇是否撞蛇身
    for snake in snakes:
        if snake.row==head.row and snake.col==head.col:
            dead = True
            break
    if dead:
        showWindow = False
    # 页面渲染
    pygame.draw.rect(window, bak_color, (0, 0, W, H))
    # 这里需要注意 绘制食物与蛇头要在绘制背景之后 因为黑色的背景颜色会覆盖一切
    # 画蛇头
    rect(head, head_color)
    # 画蛇身
    for snake in snakes:
        rect(snake, snake_color)
    # 画食物
    rect(food, food_color)
    pygame.display.flip() #更新整个待显示的Surface对象到屏幕上

    clock.tick(30)# 设置帧频 可以用来控制蛇头移动的速度

