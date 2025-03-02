import pygame
import random

# Настройки игры
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


# Класс для корабля
class Ship:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 70, 50)  # Прямоугольник корабля
        self.hp = 100  # Очки здоровья
        self.projectiles = 5  # Количество снарядов

    def draw(self, screen):
        pygame.draw.rect(screen, GREEN if self.hp > 0 else RED, self.rect)  # Рисуем корабль
        self.display_hp(screen)

    def display_hp(self, screen):
        hp_text = font.render(f'HP: {self.hp}', True, BLACK)
        screen.blit(hp_text, (self.rect.x, self.rect.y - 20))


# Класс для снаряда
class Projectile:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 5, 10)  # Прямоугольник снаряда

    def update(self):
        self.rect.y -= 10  # Движение снаряда вверх

    def draw(self, screen):
        pygame.draw.rect(screen, BLACK, self.rect)


# Инициализация Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Морской бой")
font = pygame.font.SysFont(None, 36)
clock = pygame.time.Clock()

# Игрок и противник
player = Ship(SCREEN_WIDTH // 2 - 35, SCREEN_HEIGHT - 60)
enemy = Ship(SCREEN_WIDTH // 2 - 35, 40)

# Список снарядов
projectiles = []

running = True
while running:
    screen.fill(WHITE)  # Очистка экрана

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Обработка нажатия клавиш
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player.projectiles > 0:
                projectiles.append(Projectile(player.rect.centerx, player.rect.top))
                player.projectiles -= 1

    # Обновление снарядов
    for projectile in projectiles[:]:
        projectile.update()
        if projectile.rect.y < 0:
            projectiles.remove(projectile)
        elif projectile.rect.colliderect(enemy.rect):
            enemy.hp -= 10  # Уменьшение HP противника
            projectiles.remove(projectile)

    # Отрисовка кораблей
    player.draw(screen)
    enemy.draw(screen)

    # Отрисовка снарядов
    for projectile in projectiles:
        projectile.draw(screen)

    pygame.display.flip()  # Обновление дисплея
    clock.tick(FPS)  # Установка FPS

pygame.quit()
