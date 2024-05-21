import random
from typing import Sequence


class SpriteFactory:
    @classmethod
    def generate(cls, sprites: type | Sequence[type], count: int):
        rand_list = random.choices(sprites, k=count)
        return [sprite() for sprite in rand_list]
