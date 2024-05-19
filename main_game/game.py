import pygame
import sys

from bubble_hunt.game import run_bubble_hunt
from main_game.peach import Peach
from mur_tv.game import run_murtv
from utils.colors import BLACK, WHITE, GREEN

pygame.init()

screen_width, screen_height = 1920, 1080
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

font = pygame.font.Font(None, 74)

start_button = pygame.Rect(screen_width // 2 - 150, screen_height // 2 - 50, 300, 100)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)


def main_menu():
    while True:
        screen.fill(BLACK)
        draw_text('Main Menu', font, WHITE, screen, screen_width // 2, screen_height // 2 - 150)

        pygame.draw.rect(screen, GREEN, start_button)
        draw_text('Начать игру', font, BLACK, screen, screen_width // 2, screen_height // 2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    game()

        pygame.display.update()


background = pygame.image.load('main_game/assets/map.jpg')
background = pygame.transform.scale(background, (screen_width, screen_height))
collision_map = pygame.image.load('main_game/assets/collision_map.jpg')  # Убедитесь, что размер соответствует
collision_map = pygame.transform.scale(collision_map, (screen_width, screen_height))  # Масштабируем карту коллизий

tv_zone = pygame.Rect(
    450,
    500,
    100,
    200
)
bath_zone = pygame.Rect(
    870,
    450,
    300,
    150
)


def game():
    peach = Peach(865, 900, collision_map)
    clock = pygame.time.Clock()

    running = True
    while running:
        dt = clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        peach.update(keys, dt)

        screen.blit(background, (0, 0))  # Рисуем фон
        peach.draw(screen)  # Рисуем персонажа

        if peach.rect.colliderect(bath_zone):
            draw_text('Для игры нажмите E', font, WHITE, screen, screen_width // 2, screen_height - 50)
            if keys[pygame.K_e]:
                run_bubble_hunt(screen)

        if peach.rect.colliderect(tv_zone):
            draw_text('Для игры нажмите E', font, WHITE, screen, screen_width // 2, screen_height - 50)
            if keys[pygame.K_e]:
                run_murtv(screen)

        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main_menu()
