import pygame
import random
import sys

# Assuming MUR_TV_SETTINGS is a module that contains your game settings
from mur_tv.config import MUR_TV_SETTINGS

pygame.init()

SCREEN = pygame.display.set_mode(MUR_TV_SETTINGS.SCREEN.BACKGROUND.SIZE.to_tuple)
pygame.display.set_caption(MUR_TV_SETTINGS.SCREEN.DISPLAY_NAME)
FONT = pygame.font.Font(None, MUR_TV_SETTINGS.SCREEN.FONT_SIZE)

BACKGROUND_IMAGE = pygame.transform.scale(
    pygame.image.load(MUR_TV_SETTINGS.SCREEN.BACKGROUND.IMAGE),
    MUR_TV_SETTINGS.SCREEN.BACKGROUND.SIZE.to_tuple
)

CHANNEL_WITH_MICE = random.randint(1, 10)
CURRENT_CHANNEL = 1
KEY_COUNT = 0
GAME_OVER = False

tv_rect = pygame.Rect(278, 172, 318, 172)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    SCREEN.blit(BACKGROUND_IMAGE, (0, 0))
    channel_surface = pygame.Surface((tv_rect.width, tv_rect.height))
    channel_surface.fill((255, 0, 0))
    channel_surface.set_alpha(160)
    SCREEN.blit(channel_surface, tv_rect.topleft)
    pygame.display.flip()

pygame.quit()
sys.exit()
