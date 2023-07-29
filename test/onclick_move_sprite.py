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

class DraggableSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, draggable=True):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(RED)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.draggable = draggable
        self.offset_x, self.offset_y = 0, 0
        self.dragging = False

    def update(self):
        if self.dragging:
            self.rect.x, self.rect.y = pygame.mouse.get_pos()[0] - self.offset_x, pygame.mouse.get_pos()[1] - self.offset_y

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.draggable:
            if self.rect.collidepoint(event.pos):
                self.dragging = True
                self.offset_x = event.pos[0] - self.rect.x
                self.offset_y = event.pos[1] - self.rect.y
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False


# 创建Sprite组
all_sprites = pygame.sprite.Group()

# 创建一个可拖拽的Sprite，并将其添加到组中
draggable_sprite = DraggableSprite(screen_width // 2 - 50, screen_height // 2 - 25, 100, 50)
all_sprites.add(draggable_sprite)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            # 将事件传递给所有Sprite，让它们自行处理
            for sprite in all_sprites:
                sprite.handle_event(event)

    # 更新所有Sprite
    all_sprites.update()

    # 绘制背景和所有Sprite
    screen.fill(WHITE)
    all_sprites.draw(screen)

    # 更新屏幕显示
    pygame.display.flip()

pygame.quit()
sys.exit()
