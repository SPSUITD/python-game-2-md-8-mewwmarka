import random



class SpriteFactory:
    @classmethod
    def generate(cls, sprites, count: int):
        rand_list = random.choices(sprites, k=count)
        return [sprite() for sprite in rand_list]
