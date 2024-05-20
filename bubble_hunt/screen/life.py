from pygame import Surface
from pygame.font import Font


def draw_lives(
        screen: Surface,
        image: Surface,
        lives: int,
        start_x: int,
        start_y: int,
        spacing: int | None = 60
):
    for i in range(lives):
        img_x = start_x + (i * spacing)
        img_y = start_y
        screen.blit(image, (img_x, img_y))


def draw_score(
        screen: Surface,
        font: Font,
        score: int,
        start_x: int,
        start_y: int,

):
    score_surface = font.render(f'Score: {score}/25', True, (255, 255, 255))
    screen.blit(score_surface, (start_x, start_y))
