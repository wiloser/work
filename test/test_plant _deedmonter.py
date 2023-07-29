import pygame
import sys

pygame.init()

# 设置窗口尺寸
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("植物大战僵尸 - 拖动和种植植物")

# 定义颜色
WHITE = (255, 255, 255)
BLUE1 = (0, 255, 0)
BLUE = (0, 0, 255)

# 定义植物类
class Plant(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(BLUE1)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.dragging = False

    def update(self):
        if self.dragging:
            self.rect.center = pygame.mouse.get_pos()

# 创建植物图标
plant_icon = Plant(50, 50)

# 创建植物种植区域的槽位
slot_width, slot_height = 50, 50
slot_spacing = 20
num_slots = 3
slot_x_start = screen_width // 2 - (num_slots * (slot_width + slot_spacing)) // 2

slots = []
for i in range(num_slots):
    slot_x = slot_x_start + i * (slot_width + slot_spacing)
    slot_y = screen_height - 100
    slot_rect = pygame.Rect(slot_x, slot_y, slot_width, slot_height)
    slots.append(slot_rect)

# 创建Sprite组
all_sprites = pygame.sprite.Group()
all_sprites.add(plant_icon)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 如果点击了植物图标，启动拖拽
            if plant_icon.rect.collidepoint(event.pos):
                plant_icon.dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if plant_icon.dragging:
                # 检查植物是否被拖拽到某个槽位内
                for slot in slots:
                    if slot.collidepoint(event.pos):
                        # 种植植物在槽位中心
                        plant_icon.rect.center = slot.center
                plant_icon.dragging = False

    # 更新植物位置
    all_sprites.update()

    # 绘制背景、槽位和植物图标
    screen.fill(WHITE)
    for slot in slots:
        pygame.draw.rect(screen, BLUE, slot)
    all_sprites.draw(screen)

    # 更新屏幕显示
    pygame.display.flip()

pygame.quit()
sys.exit()
