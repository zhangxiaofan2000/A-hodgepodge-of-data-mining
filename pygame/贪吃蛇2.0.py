# -*- coding: utf-8 -*-
# Auther : ZhangYiLong
# Mail : 503302425@qq.com
# Date : 2023/2/10 17:27
# File : 贪吃蛇2.0.py
import random
import time
import pygame

# 定义显示窗口的W(宽) H(高)
W = 600
H = 600
ROW = 30 #行数
COL = 30 #列数
size = (W, H)
pygame.init() # 初始化界面
window = pygame.display.set_mode(size)
pygame.display.set_caption("贪吃蛇大作战")



WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
font = pygame.font.Font("./resources/font/SIMYOU.TTF", 36)


def menu():
    # Load font
    # Render text for buttons
    start_text = font.render("开始", True, BLACK)
    settings_text = font.render("设置", True, BLACK)
    quit_text = font.render("退出", True, BLACK)
    # Get rectangles for buttons
    start_rect = start_text.get_rect()
    settings_rect = settings_text.get_rect()
    quit_rect = quit_text.get_rect()
    # Position buttons
    start_rect.center = (200, 100)
    settings_rect.center = (200, 150)
    quit_rect.center = (200, 200)
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                # Get mouse position
                pos = pygame.mouse.get_pos()
                # Check if start button was clicked
                if start_rect.collidepoint(pos):
                    start_game()
                    print("Start Game")
                # Check if settings button was clicked
                if settings_rect.collidepoint(pos):
                    print("Settings")
                # Check if quit button was clicked
                if quit_rect.collidepoint(pos):
                    running = False

        # Clear screen
        window.fill(WHITE)

        # Draw buttons
        window.blit(start_text, start_rect)
        window.blit(settings_text, settings_rect)
        window.blit(quit_text, quit_rect)

        pygame.display.update()




class Point:
    def __init__(self, row=0, col=0):
        self.row = row
        self.col = col
    def copy(self):
        return Point(self.row, self.col)
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
def rect(point, color):
    cell_width = W/COL
    cell_height = H/ROW
    left = point.col*cell_width
    top = point.row*cell_height
    pygame.draw.rect(
        window, color,
        (left, top, cell_width, cell_height)
    )

def start_game():
    size = (W, H)
    window = pygame.display.set_mode(size)
    bak_color = (255, 255, 255)
    # 定义蛇头
    head = Point(row=int(ROW / 2), col=int(COL / 2))
    head_color = (0, 128, 128)
    # 定义食物
    foods=[]
    for _ in range(20):
        food = ge_food()
        foods.append(food)
    food_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    snake_color = (128, 128, 128)
    direct = 'left'

    # Set the initial speed of the snake
    speed = 7

    # Set the initial time
    last_move = time.time()


    snake_speed = 1





    def rect(point, color):
        cell_width = W / COL
        cell_height = H / ROW
        left = point.col * cell_width
        top = point.row * cell_height
        pygame.draw.rect(
            window, color,
            (left, top, cell_width, cell_height)
        )

    showWindow = True
    clock = pygame.time.Clock()  # 时钟控制
    while showWindow:
        # 处理事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                showWindow = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if direct == 'left' or direct == 'right':
                        direct = "top"
                elif event.key == pygame.K_DOWN:
                    if direct == 'left' or direct == 'right':
                        direct = "down"
                elif event.key == pygame.K_LEFT:
                    if direct == 'top' or direct == 'down':
                        direct = 'left'
                elif event.key == pygame.K_RIGHT:
                    if direct == 'top' or direct == 'down':
                        direct = 'right'



        current_time = time.time()
        if current_time - last_move > 1 / speed:
            last_move = current_time
            # 判断蛇是否吃到东西
            eat = False
            for food in foods:
                if head.row == food.row and head.col == food.col:  # 蛇吃到食物
                    snake_color = food_color
                    food_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                    eat = True
                if eat:  # 吃到食物就要产生新的食物
                    foods.remove(food)
                    food = ge_food()
                    foods.append(food)

            # 将蛇头插入到snakes列表中
            snakes.insert(0, head.copy())
            # 将最后一个元素删除
            if not eat:
                snakes.pop()

            # 移动蛇头
            if direct == 'left':
                head.col -= 1  # 注意 direct = 'left'与head.col-=1不能写在一起 因为蛇头要一直移动
            elif direct == 'right':
                head.col += 1
            elif direct == 'top':
                head.row -= 1
            else:
                head.row += 1
            # 判断蛇是否死亡
            dead = False
            # 判断蛇是否撞墙
            if head.col < 0:
                head.col = COL
            if head.row < 0:
                head.row = ROW

            if head.col > COL:
                head.col = 0
            if head.row > ROW:
                head.row = 0
            # if head.col < 0 or head.row < 0 or head.row >= ROW or head.col >= COL:
                # Render text
                # game_over_text = font.render("游戏结束：撞墙", True, BLACK)
                # game_over_text_rect = game_over_text.get_rect()
                # game_over_text_rect.center = (200, 150)
                # dead = True
            # 判断蛇是否撞蛇身
            for snake in snakes:
                if snake.row == head.row and snake.col == head.col:
                    # Render text
                    game_over_text = font.render("游戏结束：撞蛇身", True, BLACK)
                    game_over_text_rect = game_over_text.get_rect()
                    game_over_text_rect.center = (200, 150)

                    dead = True
                    break
            if dead:
                showWindow = False


        # 页面渲染
        pygame.draw.rect(window, bak_color, (0, 0, W, H))
        # 这里需要注意 绘制食物与蛇头要在绘制背景之后 因为黑色的背景颜色会覆盖一切
        # 画蛇头
        rect(head, head_color)

        # 画食物
        for food in foods:
            rect(food, food_color)

        # 画蛇身
        for snake in snakes:
            rect(snake, snake_color)

        pygame.display.flip()  # 更新整个待显示的Surface对象到屏幕上

        clock.tick(120)
    snakes.clear()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                # Get mouse position
                pos = pygame.mouse.get_pos()
                # Check if start button was clicked
                if game_over_text_rect.collidepoint(pos):
                    running = False

        # Clear screen
        window.fill(WHITE)
        window.blit(game_over_text, game_over_text_rect)
        pygame.display.update()




if __name__ == '__main__':
    snakes = []  # 定义蛇身列表
    bak_color = (255, 255, 255)
    # 定义蛇头
    head = Point(row=int(ROW / 2), col=int(COL / 2))
    head_color = (0, 128, 128)
    # 定义食物
    food = ge_food()
    food_color = (255, 255, 0)

    snake_color = (128, 128, 128)
    direct = 'left'

    menu()