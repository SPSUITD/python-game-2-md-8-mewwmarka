import pygame
import sys

from bubble_hunt.game import run_bubble_hunt
from freezer.game import run_freezer
from main_game.peach import Peach
from mur_tv.game import run_murtv
from utils.colors import BLACK, WHITE

pygame.init()

screen_width, screen_height = 1920, 1080
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

font = pygame.font.Font(None, 74)

menu_image = pygame.image.load('main_game/assets/main_menu.png')
scale_factor = 0.3
menu_image = pygame.transform.scale(menu_image, (int(menu_image.get_width() * scale_factor), int(menu_image.get_height() * scale_factor)))
menu_image_rect = menu_image.get_rect(center=(screen_width // 2, screen_height // 2))

start_button_width = 500
start_button_height = 300
start_button_x = menu_image_rect.left + (menu_image_rect.width - start_button_width) // 2
start_button_y = menu_image_rect.top + (menu_image_rect.height - start_button_height) // 1.8
start_button_rect = pygame.Rect(start_button_x, start_button_y, start_button_width, start_button_height)


win_image = pygame.image.load('main_game/assets/win.png')
win_image = pygame.transform.scale(win_image, (890, 745))

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

def main_menu():
    while True:
        screen.fill(BLACK)
        screen.blit(menu_image, menu_image_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button_rect.collidepoint(event.pos):
                    game()

        pygame.display.update()

background = pygame.image.load('main_game/assets/map.jpg')
background = pygame.transform.scale(background, (screen_width, screen_height))
collision_map = pygame.image.load('main_game/assets/collision_map.jpg')
collision_map = pygame.transform.scale(collision_map, (screen_width, screen_height))

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
freezer_zone = pygame.Rect(
    1100,
    150,
    150,
    150
)

key_image = pygame.image.load('main_game/assets/key.png')
key_image = pygame.transform.scale(key_image, (100, 100))


def draw_collected_keys(screen, keys_collected):
    x_start = screen_width - 150
    y_start = 30
    progress_font = pygame.font.Font(None, 48)

    collected_count = sum(keys_collected.values())
    progress_text = f'{collected_count}/3'

    screen.blit(key_image, (x_start, y_start))
    draw_text(progress_text, progress_font, WHITE, screen, x_start + 50, y_start + 100)

def draw_winner_screen():
    screen.fill(BLACK)
    screen.blit(win_image, (512, 167))
    pygame.display.update()
    pygame.time.wait(5000)
    main_menu()


def pause_menu():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

        screen.fill(BLACK)
        draw_text('Paused', font, WHITE, screen, screen_width // 2, screen_height // 2 - 50)
        draw_text('Press ESC to resume or Q to quit', font, WHITE, screen, screen_width // 2, screen_height // 2 + 50)
        pygame.display.update()

def game():
    peach = Peach(865, 900, collision_map)
    clock = pygame.time.Clock()

    keys_collected = {
        'bath_key': False,
        'tv_key': False,
        'freezer_key': False
    }

    running = True
    while running:
        dt = clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause_menu()

        keys = pygame.key.get_pressed()
        peach.update(keys, dt)

        screen.blit(background, (0, 0))
        peach.draw(screen)

        if peach.rect.colliderect(bath_zone):
            text = 'Для игры нажмите E' if not keys_collected['bath_key'] else 'Ключ найден!'
            draw_text(text, font, WHITE, screen, screen_width // 2, screen_height - 50)
            if not keys_collected['bath_key'] and keys[pygame.K_e] and run_bubble_hunt(screen):
                keys_collected['bath_key'] = True

        if peach.rect.colliderect(tv_zone):
            text = 'Для игры нажмите E' if not keys_collected['tv_key'] else 'Ключ найден!'
            draw_text(text, font, WHITE, screen, screen_width // 2, screen_height - 50)
            if not keys_collected['tv_key'] and keys[pygame.K_e] and run_murtv(screen):
                keys_collected['tv_key'] = True

        if peach.rect.colliderect(freezer_zone):
            text = 'Для игры нажмите E' if not keys_collected['freezer_key'] else 'Ключ найден!'
            draw_text(text, font, WHITE, screen, screen_width // 2, screen_height - 50)
            if not keys_collected['freezer_key'] and keys[pygame.K_e] and run_freezer(screen):
                keys_collected['freezer_key'] = True

        draw_collected_keys(screen, keys_collected)

        if all(keys_collected.values()):
            draw_winner_screen()

        pygame.display.update()
    pygame.quit()


if __name__ == '__main__':
    main_menu()
