import pygame
import sys

pygame.init()

# 设置窗口尺寸
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("拖拽效果示例")

# 定义颜色
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# 创建一个矩形
rect_width, rect_height = 100, 50
rect = pygame.Rect(screen_width // 2 - rect_width // 2, screen_height // 2 - rect_height // 2, rect_width, rect_height)

dragging = False
offset_x, offset_y = 0, 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                dragging = True
                offset_x = event.pos[0] - rect.x
                offset_y = event.pos[1] - rect.y
        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = False

    if dragging:
        # 鼠标拖动时更新矩形的位置
        rect.x, rect.y = pygame.mouse.get_pos()[0] - offset_x, pygame.mouse.get_pos()[1] - offset_y

    # 绘制背景和矩形
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, rect)

    # 更新屏幕显示
    pygame.display.flip()
