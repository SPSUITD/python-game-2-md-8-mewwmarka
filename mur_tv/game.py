import pygame
import random
import sys
import cv2

from mur_tv.config import MUR_TV_SETTINGS

pygame.init()

SCREEN = pygame.display.set_mode(MUR_TV_SETTINGS.SCREEN.BACKGROUND.SIZE.to_tuple)
pygame.display.set_caption(MUR_TV_SETTINGS.SCREEN.DISPLAY_NAME)
FONT = pygame.font.Font(None, MUR_TV_SETTINGS.SCREEN.FONT_SIZE)

BACKGROUND_IMAGE = pygame.transform.scale(
    pygame.image.load(MUR_TV_SETTINGS.SCREEN.BACKGROUND.IMAGE),
    MUR_TV_SETTINGS.SCREEN.BACKGROUND.SIZE.to_tuple
)

caps = [cv2.VideoCapture(path) for path in MUR_TV_SETTINGS.SCREEN.IMAGES]
mice_image = pygame.image.load(MUR_TV_SETTINGS.SCREEN.MICE_IMAGE)
mice_image = pygame.transform.scale(mice_image, (50, 50))

channel_with_mice = random.randint(0, len(caps) - 1)

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
MICE_POSITION = None
RUNNING = True

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
        if not MICE_POSITION:
            mice_x = random.randint(tv_rect.left, tv_rect.right - mice_image.get_width())
            mice_y = random.randint(tv_rect.top, tv_rect.bottom - mice_image.get_height())
            MICE_POSITION = (mice_x, mice_y)
        SCREEN.blit(mice_image, MICE_POSITION)
    pygame.display.flip()

for cap in caps:
    cap.release()

pygame.quit()
sys.exit()
