import pygame


class Peach(pygame.sprite.Sprite):
    def __init__(self, x, y, collision_map):
        super().__init__()

        self.original_frames = [pygame.image.load(f'main_game/assets/peach_{i}-01.png') for i in range(1, 4)]
        self.frames = [pygame.transform.scale(frame, (100*0.75, 150*0.75)) for frame in self.original_frames]
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect(center=(x, y))
        self.animation_timer = 0
        self.direction = 'up'
        self.collision_map = collision_map

    def rotate_frames(self, angle):

        self.frames = [pygame.transform.rotate(pygame.transform.scale(frame, (100*0.75, 150*0.75)), angle) for frame in
                       self.original_frames]

    def check_collision(self, dx, dy):

        new_rect = self.rect.move(dx, dy)
        for x in range(new_rect.left, new_rect.right):
            for y in range(new_rect.top, new_rect.bottom):
                if self.collision_map.get_at((x, y))[0] == 0:
                    return True
        return False

    def update(self, keys, dt):
        new_direction = self.direction
        dx, dy = 0, 0

        if keys[pygame.K_LEFT]:
            new_direction = 'left'
            dx = -5
        elif keys[pygame.K_RIGHT]:
            new_direction = 'right'
            dx = 5
        elif keys[pygame.K_UP]:
            new_direction = 'up'
            dy = -5
        elif keys[pygame.K_DOWN]:
            new_direction = 'down'
            dy = 5


        if new_direction != self.direction:
            if new_direction == 'left':
                angle = 90
            elif new_direction == 'right':
                angle = -90
            elif new_direction == 'down':
                angle = 180
            elif new_direction == 'up':
                angle = 0
            self.rotate_frames(angle)
            self.direction = new_direction

        if not self.check_collision(dx, dy):
            self.rect.x += dx
            self.rect.y += dy


            if dx != 0 or dy != 0:
                self.animation_timer += dt
                if self.animation_timer > 100:
                    self.current_frame = (self.current_frame + 1) % len(self.frames)
                    self.image = self.frames[self.current_frame]
                    self.animation_timer = 0

    def draw(self, surface):
        surface.blit(self.image, self.rect)
