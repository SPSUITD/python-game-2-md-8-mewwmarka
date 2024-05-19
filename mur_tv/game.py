import pygame
import random
import sys
import cv2

from mur_tv.config import MUR_TV_SETTINGS
from utils.popups import show_popup

pygame.init()

SCREEN = pygame.display.set_mode(MUR_TV_SETTINGS.SCREEN.BACKGROUND.SIZE.to_tuple)
pygame.display.set_caption(MUR_TV_SETTINGS.SCREEN.DISPLAY_NAME)
FONT = pygame.font.Font(None, MUR_TV_SETTINGS.SCREEN.FONT_SIZE)

BACKGROUND_IMAGE = pygame.transform.scale(
    pygame.image.load(MUR_TV_SETTINGS.SCREEN.BACKGROUND.IMAGE),
    MUR_TV_SETTINGS.SCREEN.BACKGROUND.SIZE.to_tuple
)

channel_paths = list(MUR_TV_SETTINGS.SCREEN.CHANNELS)
random.shuffle(channel_paths)
caps = [cv2.VideoCapture(path) for path in channel_paths]
channel_with_mice = channel_paths.index(MUR_TV_SETTINGS.SCREEN.MICE_CHANNEL)

tv_rect = pygame.Rect(278, 172, 318, 172)


def get_frame(cap):
    ret, frame = cap.read()
    if not ret:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        ret, frame = cap.read()
    if not ret:
        return None
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = cv2.resize(frame, (tv_rect.width, tv_rect.height))
    return pygame.transform.rotate(pygame.surfarray.make_surface(frame), -90)


CURRENT_VIDEO_INDEX = 0
RUNNING = True
WIN = False

while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                CURRENT_VIDEO_INDEX = (CURRENT_VIDEO_INDEX + 1) % len(caps)
            elif event.key == pygame.K_LEFT:
                CURRENT_VIDEO_INDEX = (CURRENT_VIDEO_INDEX - 1) % len(caps)

    SCREEN.blit(BACKGROUND_IMAGE, (0, 0))
    video_surface = get_frame(caps[CURRENT_VIDEO_INDEX])
    if video_surface:
        SCREEN.blit(video_surface, tv_rect.topleft)

    if CURRENT_VIDEO_INDEX == channel_with_mice:
        WIN = True
        show_popup(SCREEN, "Вы нашли мышь! Нажмите Enter для выхода.")
        break
    pygame.display.flip()

for cap in caps:
    cap.release()

pygame.quit()
sys.exit()
