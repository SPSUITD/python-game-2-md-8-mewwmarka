import pygame


class Camera:
    def __init__(self, camera_width, camera_height, map_width, map_height, zoom_factor=1.5):
        self.camera_rect = pygame.Rect(0, 0, int(camera_width / zoom_factor), int(camera_height / zoom_factor))
        self.map_width = map_width
        self.map_height = map_height
        self.zoom_factor = zoom_factor

    def apply(self, entity):
        # Проверяем, является ли объект спрайтом
        if hasattr(entity, 'rect'):
            # Применяем смещение камеры к rect спрайта
            return entity.rect.move(-self.camera_rect.x, -self.camera_rect.y)
        else:
            # Применяем смещение камеры напрямую к прямоугольнику
            return entity.move(-self.camera_rect.x, -self.camera_rect.y)

    def update(self, target):
        self.camera_rect.center = target.rect.center
        self.camera_rect.clamp_ip(pygame.Rect(0, 0, self.map_width, self.map_height))
