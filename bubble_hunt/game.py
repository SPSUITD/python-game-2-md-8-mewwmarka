import pygame
from bubble_hunt.config import bubble_settings
from bubble_hunt.screen.life import draw_lives, draw_score
from bubble_hunt.sprites.factory import SpriteFactory
from bubble_hunt.sprites.sprite import Sponge, Shampoo, Bubble, Soap
from utils.popups import show_popup


def run_bubble_hunt(screen):

    clock = pygame.time.Clock()
    background_image = pygame.transform.scale(
        pygame.image.load(bubble_settings.SCREEN.BACKGROUND.IMAGE).convert(),
        bubble_settings.SCREEN.BACKGROUND.SIZE.to_tuple
    )
    life_image = pygame.transform.scale(
        pygame.image.load(bubble_settings.SCREEN.LIFE_IMAGE.IMAGE).convert_alpha(),
        bubble_settings.SCREEN.LIFE_IMAGE.SIZE.to_tuple
    )

    font = pygame.font.Font(None, 36)

    all_sprites = pygame.sprite.Group()
    bubbles = pygame.sprite.Group()
    enemies = pygame.sprite.Group()

    bubbles.add(SpriteFactory.generate([Bubble], 10))
    enemies.add(SpriteFactory.generate([Soap, Shampoo, Sponge], 10))
    all_sprites.add(*enemies.sprites(), *bubbles.sprites())

    lives = bubble_settings.GAME.LIVES
    score = 0
    is_running = True
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked_bubbles = [b for b in bubbles if b.rect.collidepoint(pos)]
                clicked_enemies = [s for s in enemies if s.rect.collidepoint(pos)]
                for bubble in clicked_bubbles:
                    bubble.reset_position()
                    score += 1
                    if score >= 25:
                        show_popup(screen, "Вы лопнули пузыри! Нажмите Enter для выхода.")
                        return True
                for enemy in clicked_enemies:
                    enemy.kill()
                    lives -= 1
                    if lives <= 0:
                        show_popup(screen, f"Игра окончена! Ваш счет: {score}")
                        return False
        all_sprites.update()
        screen.blit(background_image, (0, 0))
        all_sprites.draw(screen)
        draw_lives(screen=screen, lives=lives, image=life_image, start_x=10, start_y=10)
        draw_score(screen=screen, score=score, font=font, start_x=800 - 150, start_y=10)
        pygame.display.flip()
        clock.tick(bubble_settings.SCREEN.FPS)
