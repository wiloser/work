import pygame
import sys

pygame.init()

# 设置屏幕大小和其他必要的参数
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("键盘输入检测测试")
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            print(f"Key pressed: {event.key}")

    # 绘制背景
    screen.fill((255, 255, 255))
    pygame.display.flip()

    # 控制帧率
    clock.tick(60)
