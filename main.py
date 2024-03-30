import pygame
import random

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Пузырьковая охота')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

lives = 3
score = 0


bubble_image = pygame.image.load('placeholder.png').convert_alpha()
soap_image = pygame.image.load('placeholder.png').convert_alpha()


# Создание спрайтов
class Bubble(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(bubble_image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.rect.y = random.randint(0, screen_height - self.rect.height)


class Soap(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(soap_image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.rect.y = random.randint(0, screen_height - self.rect.height)


all_sprites = pygame.sprite.Group()
bubbles = pygame.sprite.Group()
soaps = pygame.sprite.Group()

for _ in range(10):
    bubble = Bubble()
    all_sprites.add(bubble)
    bubbles.add(bubble)

for _ in range(5):
    soap = Soap()
    all_sprites.add(soap)
    soaps.add(soap)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            clicked_bubbles = [b for b in bubbles if b.rect.collidepoint(pos)]
            clicked_soaps = [s for s in soaps if s.rect.collidepoint(pos)]
            for bubble in clicked_bubbles:
                bubble.kill()
                score += 1
            for soap in clicked_soaps:
                soap.kill()
                lives -= 1
                if lives <= 0:
                    print("Игра окончена! Ваш счет:", score)
                    running = False

    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
