import random
from typing import Sequence


class SpriteFactory:
    @classmethod
    def generate[T](cls, sprites: type[T] | Sequence[type[T]], count: int) -> T:
        rand_list = random.choices(sprites, k=count)
        return [sprite() for sprite in rand_list]
