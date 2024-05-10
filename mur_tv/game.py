import pygame
import random
import sys
import cv2

from mur_tv.config import MUR_TV_SETTINGS

# Initialize Pygame
pygame.init()

# Setup the screen
SCREEN = pygame.display.set_mode(MUR_TV_SETTINGS.SCREEN.BACKGROUND.SIZE.to_tuple)
pygame.display.set_caption(MUR_TV_SETTINGS.SCREEN.DISPLAY_NAME)
FONT = pygame.font.Font(None, MUR_TV_SETTINGS.SCREEN.FONT_SIZE)

# Load and scale the background image
BACKGROUND_IMAGE = pygame.transform.scale(
    pygame.image.load(MUR_TV_SETTINGS.SCREEN.BACKGROUND.IMAGE),
    MUR_TV_SETTINGS.SCREEN.BACKGROUND.SIZE.to_tuple
)

# Load videos
caps = [cv2.VideoCapture(path) for path in MUR_TV_SETTINGS.SCREEN.IMAGES]
current_video_index = 0

# Define the TV screen area
tv_rect = pygame.Rect(278, 172, 318, 172)  # Adjust these values to fit your background's TV area


def get_frame(cap):
    ret, frame = cap.read()
    if not ret:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        ret, frame = cap.read()
    if not ret:
        return None
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = cv2.resize(frame, (tv_rect.width, tv_rect.height))  # Resize to fit the TV area
    return pygame.transform.rotate(pygame.surfarray.make_surface(frame), -90)

# Main game loop
RUNNING = True
while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                current_video_index = (current_video_index + 1) % len(caps)
            elif event.key == pygame.K_LEFT:
                current_video_index = (current_video_index - 1) % len(caps)

    SCREEN.blit(BACKGROUND_IMAGE, (0, 0))  # Blit the background first
    video_surface = get_frame(caps[current_video_index])
    if video_surface:
        SCREEN.blit(video_surface, tv_rect.topleft)  # Blit the video on the TV area

    pygame.display.flip()

# Clean up
for cap in caps:
    cap.release()
pygame.quit()
sys.exit()
