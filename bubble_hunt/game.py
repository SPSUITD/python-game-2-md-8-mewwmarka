import pygame

from bubble_hunt.config import bubble_settings
from bubble_hunt.screen.life import draw_lives, draw_score
from bubble_hunt.sprites.factory import SpriteFactory
from bubble_hunt.sprites.sprite import Sponge, Shampoo, Bubble, Soap
from utils.popups import show_popup

pygame.init()

CLOCK = pygame.time.Clock()
SCREEN = pygame.display.set_mode(bubble_settings.SCREEN.BACKGROUND.SIZE.to_tuple)
BACKGROUND_IMAGE = pygame.transform.scale(
    pygame.image.load(bubble_settings.SCREEN.BACKGROUND.IMAGE).convert(),
    bubble_settings.SCREEN.BACKGROUND.SIZE.to_tuple
)
LIFE_IMAGE = pygame.transform.scale(
    pygame.image.load(bubble_settings.SCREEN.LIFE_IMAGE.IMAGE).convert_alpha(),
    bubble_settings.SCREEN.LIFE_IMAGE.SIZE.to_tuple
)
pygame.display.set_caption(bubble_settings.SCREEN.DISPLAY_NAME)

FONT = pygame.font.Font(None, 36)


ALL_SPRITES = pygame.sprite.Group()
BUBBLES = pygame.sprite.Group()
ENEMIES = pygame.sprite.Group()

BUBBLES.add(SpriteFactory.generate([Bubble], 10))
ENEMIES.add(SpriteFactory.generate([Soap, Shampoo, Sponge], 10))
ALL_SPRITES.add(*ENEMIES.sprites(), *BUBBLES.sprites())

LIVES = bubble_settings.GAME.LIVES
SCORE = 0
IS_RUNNING = True
while IS_RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            IS_RUNNING = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            clicked_bubbles = [b for b in BUBBLES if b.rect.collidepoint(pos)]
            clicked_enemies = [s for s in ENEMIES if s.rect.collidepoint(pos)]
            for bubble in clicked_bubbles:
                bubble.reset_position()
                SCORE += 1
                if SCORE >= 25:
                    show_popup(SCREEN, "Вы лопнули пузыри! Нажмите Enter для выхода.")
                    IS_RUNNING = False
            for soap in clicked_enemies:
                soap.kill()
                LIVES -= 1
                if LIVES <= 0:
                    show_popup(SCREEN, f"Игра окончена! Ваш счет: {SCORE}")
                    IS_RUNNING = False

    ALL_SPRITES.update()
    SCREEN.blit(BACKGROUND_IMAGE, (0, 0))
    ALL_SPRITES.draw(SCREEN)
    draw_lives(screen=SCREEN, lives=LIVES, image=LIFE_IMAGE, start_x=10, start_y=10)
    draw_score(screen=SCREEN, score=SCORE, font=FONT, start_x=SCREEN.get_width() - 150, start_y=10)
    pygame.display.flip()
    CLOCK.tick(bubble_settings.SCREEN.FPS)
pygame.quit()
