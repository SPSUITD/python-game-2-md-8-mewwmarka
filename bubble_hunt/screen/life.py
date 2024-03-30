from pygame import Surface


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
