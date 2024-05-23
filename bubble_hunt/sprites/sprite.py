from abc import ABC
from typing import ClassVar

import pygame
import random

from bubble_hunt.config import bubble_settings, Image
from bubble_hunt.value_objects import Speed


class FallingSprite(pygame.sprite.Sprite, ABC):
    SPRITE_CONFIG: Image
    SPEED_RANGE: ClassVar[Speed]

    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(
            pygame.image.load(self.SPRITE_CONFIG.IMAGE).convert_alpha(),
            self.SPRITE_CONFIG.SIZE.to_tuple
        )
        self.rect = self.image.get_rect()
        self._set_position()

    def _set_position(self):
        self.rect.x = random.randint(0, bubble_settings.SCREEN.BACKGROUND.SIZE.width - self.rect.width)
        self.rect.y = random.randint(-100, -50)
        self.speed_y = random.randint(*self.SPEED_RANGE)

    def reset_position(self):
        self._set_position()

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > bubble_settings.SCREEN.BACKGROUND.SIZE.height:
            self._set_position()



class Bubble(FallingSprite):
    SPRITE_CONFIG = bubble_settings.SPRITES.BUBBLE
    SPEED_RANGE = Speed(1, 2)


class Soap(FallingSprite):
    SPRITE_CONFIG = bubble_settings.SPRITES.SOAP
    SPEED_RANGE = Speed(3, 5)


class Shampoo(FallingSprite):
    SPRITE_CONFIG = bubble_settings.SPRITES.SHAMPOO
    SPEED_RANGE = Speed(1, 4)


class Sponge(FallingSprite):
    SPRITE_CONFIG = bubble_settings.SPRITES.SPONGE
    SPEED_RANGE = Speed(2, 3)
