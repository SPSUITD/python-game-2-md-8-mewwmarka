import pygame
import sys

from utils.popups import show_popup


def run_freezer(screen):
    # Screen dimensions
    screen_width = 800
    screen_height = 600

    freezer_surface = pygame.Surface((screen_width, screen_height))

    # Load images
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

    # Define object positions
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

    # Font for text
    font = pygame.font.Font(None, 36)

    # Game variables
    found_items = set()
    lives = 3
    items_to_find = list(objects.keys())

    def create_silhouette(image):
        silhouette = pygame.Surface(image.get_size(), pygame.SRCALPHA)
        silhouette.fill((0, 0, 0, 128))  # Black with 50% transparency
        image.blit(silhouette, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        return image

    def draw_game():
        freezer_surface.blit(background_img, (0, 0))
        for item, img in objects.items():
            if item not in found_items:
                freezer_surface.blit(img, object_positions[item])

        # Draw other objects
        if 'cake' not in found_items:
            freezer_surface.blit(cake_img, object_positions['cake'])
        if 'cola' not in found_items:
            freezer_surface.blit(cola_img, object_positions['cola'])
        if 'tomato' not in found_items:
            freezer_surface.blit(tomato_img, object_positions['tomato'])

        # Draw silhouettes
        for item, pos in silhouette_positions.items():
            if item in found_items:
                freezer_surface.blit(objects[item], pos)
            else:
                silhouette = create_silhouette(objects[item].copy())
                freezer_surface.blit(silhouette, pos)

        lives_text = font.render(f'Lives: {lives}', True, (255, 255, 255))
        freezer_surface.blit(lives_text, (screen_width - 150, 10))

        if lives <= 0:
            show_popup(screen, "Вы проиграли.")
        elif len(found_items) == len(items_to_find):
            show_popup(screen, "Победа!")

    def check_click(pos):
        global lives
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
