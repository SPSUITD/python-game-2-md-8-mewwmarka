import pygame
import random
import sys

from utils.colors import WHITE, BLACK

pygame.init()

screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("МурТв")


font = pygame.font.Font(None, 36)

channel_with_mice = random.randint(1, 10)
current_channel = 1
key_count = 0
game_over = False


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                current_channel += 1
                if current_channel > 10:
                    current_channel = 1
            elif event.key == pygame.K_LEFT:
                current_channel -= 1
                if current_channel < 1:
                    current_channel = 10

            if current_channel == channel_with_mice:
                key_count += 1
                game_over = True

    screen.fill(BLACK)
    if not game_over:
        draw_text(f'Channel: {current_channel}', font, WHITE, screen, 20, 20)
    else:
        draw_text("You found the mice!", font, WHITE, screen, 20, 20)
        draw_text(f"Keys: {key_count}", font, WHITE, screen, 20, 60)

    pygame.display.update()
