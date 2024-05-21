import pygame
import sys

from utils.popups import show_popup
from freezer.screen.life import draw_lives

def run_freezer(screen):

    screen_width = 800
    screen_height = 600

    freezer_surface = pygame.Surface((screen_width, screen_height))


    background_img = pygame.image.load('freezer/assets/background.jpg')
    background_img = pygame.transform.scale(background_img, (screen_width, screen_height))

    cake_img = pygame.image.load('freezer/assets/cake.png')
    cake_img = pygame.transform.scale(cake_img, (screen_width // 5, screen_height // 5))

    chicken_img = pygame.image.load('freezer/assets/chicken.png')
    chicken_img = pygame.transform.scale(chicken_img, (screen_width // 5, screen_height // 5))

    cola_img = pygame.image.load('freezer/assets/cola.png')
    cola_img = pygame.transform.scale(cola_img, (screen_width // 20, screen_height // 8))

    milk_img = pygame.image.load('freezer/assets/milk.png')
    milk_img = pygame.transform.scale(milk_img, (screen_width // 7.5, screen_height // 5))

    salmon_img = pygame.image.load('freezer/assets/salmon.png')
    salmon_img = pygame.transform.scale(salmon_img, (screen_width // 5, screen_height // 5))

    tomato_img = pygame.image.load('freezer/assets/tomato.png')
    tomato_img = pygame.transform.scale(tomato_img, (screen_width // 10, screen_height // 7))

    life_img = pygame.image.load('freezer/assets/life.png')
    life_img = pygame.transform.scale(life_img, (screen_width // 12, screen_height // 11))

    objects = {
        'fish': salmon_img,
        'milk': milk_img,
        'chicken': chicken_img,
    }

    object_positions = {
        'fish': (50, 400),
        'milk': (600, 350),
        'chicken': (300, 300),
        'cake': (120, 180),
        'cola': (600, 210),
        'tomato': (120, 310),
    }

    silhouette_positions = {
        'fish': (0, -5),
        'milk': (150, -5),
        'chicken': (250, -5),
    }


    found_items = set()
    lives = 3
    items_to_find = list(objects.keys())

    def create_silhouette(image):
        silhouette = pygame.Surface(image.get_size(), pygame.SRCALPHA)
        silhouette.fill((0, 0, 0, 128))
        image.blit(silhouette, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        return image

    def draw_game():
        freezer_surface.blit(background_img, (0, 0))
        for item, img in objects.items():
            if item not in found_items:
                freezer_surface.blit(img, object_positions[item])


        if 'cake' not in found_items:
            freezer_surface.blit(cake_img, object_positions['cake'])
        if 'cola' not in found_items:
            freezer_surface.blit(cola_img, object_positions['cola'])
        if 'tomato' not in found_items:
            freezer_surface.blit(tomato_img, object_positions['tomato'])


        for item, pos in silhouette_positions.items():
            if item in found_items:
                freezer_surface.blit(objects[item], pos)
            else:
                silhouette = create_silhouette(objects[item].copy())
                freezer_surface.blit(silhouette, pos)


        draw_lives(freezer_surface, life_img, lives, screen_width - (life_img.get_width() + 10) * lives, 10, life_img.get_width() + 10)

        if lives <= 0:
            show_popup(screen, "Вы проиграли. Нажмите Enter")
        elif len(found_items) == len(items_to_find):
            show_popup(screen, "Победа! Нажмите Enter")

    def check_click(pos):
        nonlocal lives
        items_to_remove = []
        for item, rect_pos in object_positions.items():
            rect = pygame.Rect(rect_pos[0], rect_pos[1], screen_width // 10, screen_height // 10)
            if rect.collidepoint(pos):
                if item in items_to_find:
                    found_items.add(item)
                    items_to_remove.append(item)
                else:
                    lives -= 1
        for item in items_to_remove:
            del object_positions[item]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                check_click(event.pos)

        draw_game()
        screen.blit(freezer_surface, (0, 0))

        pygame.display.flip()

        if lives <= 0 or len(found_items) == len(items_to_find):
            running = False
