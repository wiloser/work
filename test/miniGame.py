import pygame
import math

pygame.init()

# 屏幕大小
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Moving Character with Circling Sprite")

# 颜色
blue_color = (0, 0, 255)
red_color = (255, 0, 0)
black_color = (0, 0, 0)

# 角色相关参数
blue_character_width, blue_character_height = 50, 50
blue_character_x, blue_character_y = screen_width // 2, screen_height // 2
blue_character_speed = 5

# 精灵相关参数
red_sprite_radius = 100
red_sprite_speed = (2 * math.pi) / 3  # 每秒转动3秒一圈，即2π弧度/3秒
red_sprite_angle = 0

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 更新角色位置
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        blue_character_x -= blue_character_speed
    if keys[pygame.K_RIGHT]:
        blue_character_x += blue_character_speed
    if keys[pygame.K_UP]:
        blue_character_y -= blue_character_speed
    if keys[pygame.K_DOWN]:
        blue_character_y += blue_character_speed

    # 更新精灵位置
    red_sprite_x = blue_character_x + blue_character_width * 0.5 + red_sprite_radius * math.cos(red_sprite_angle)
    red_sprite_y = blue_character_y + blue_character_height * 0.5 + red_sprite_radius * math.sin(red_sprite_angle)
    red_sprite_angle += red_sprite_speed / 60  # 60是帧率，使得精灵速度与帧率无关

    # 清屏
    screen.fill(black_color)

    # 绘制连接线和标注距离
    pygame.draw.line(screen, black_color,
                     (blue_character_x + blue_character_width * 0.5, blue_character_y + blue_character_height * 0.5),
                     (red_sprite_x, red_sprite_y), 2)
    distance = int(math.sqrt((red_sprite_x - blue_character_x - blue_character_width * 0.5) ** 2 + (
                red_sprite_y - blue_character_y - blue_character_height * 0.5) ** 2))
    font = pygame.font.Font(None, 30)
    text = font.render(f"Distance: {distance}px", True, black_color)
    screen.blit(text, (10, 10))

    # 绘制角色
    pygame.draw.rect(screen, blue_color,
                     (blue_character_x, blue_character_y, blue_character_width, blue_character_height))

    # 绘制精灵
    pygame.draw.circle(screen, red_color, (
        int(red_sprite_x), int(red_sprite_y)), 10)

    pygame.display.update()
    clock.tick(60)  # 设置帧率为60

pygame.quit()
