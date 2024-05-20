import sys

import pygame


def draw_text(surface, text, color, rect, font, aa=True, bkg=None):
    # Prepare the text lines and calculate total height
    lines = text.splitlines()
    font_height = font.get_linesize()
    total_height = len(lines) * font_height

    # Calculate the starting y position to center the text vertically
    y = rect.top + (rect.height - total_height) // 2

    for line in lines:
        text_surface = font.render(line, aa, color, bkg)
        text_width = text_surface.get_width()
        x = rect.left + (rect.width - text_width) // 2  # Center horizontally
        surface.blit(text_surface, (x, y))
        y += font_height



def show_popup(screen, message):
    popup_rect = pygame.Rect(50, 50, 700, 200)
    shadow_rect = pygame.Rect(55, 55, 700, 200)
    corner_radius = 20
    background_color = (60, 25, 60)
    shadow_color = (20, 20, 20)
    text_color = (255, 204, 0)
    pygame.draw.rect(screen, shadow_color, shadow_rect)
    pygame.draw.rect(screen, background_color, popup_rect, border_radius=corner_radius)
    font = pygame.font.Font(None, 36)
    draw_text(screen, message, text_color, popup_rect, font, aa=True)
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting = False

