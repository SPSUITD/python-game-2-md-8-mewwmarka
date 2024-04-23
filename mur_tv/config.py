from pydantic_settings import BaseSettings

from bubble_hunt.value_objects import Size


class Image(BaseSettings):
    IMAGE: str
    SIZE: Size = Size(0, 0)


class SpritesConfig(BaseSettings):
    BUBBLE: Image = Image(
        IMAGE='./assets/bubble.png',
        SIZE=Size(width=60, height=60)
    )
    SOAP: Image = Image(
        IMAGE='./assets/soap.png',
        SIZE=Size(width=50, height=50)
    )
    SHAMPOO: Image = Image(
        IMAGE='./assets/shampoo.png',
        SIZE=Size(width=90, height=90)
    )
    SPONGE: Image = Image(
        IMAGE='./assets/sponge.png',
        SIZE=Size(width=70, height=70)
    )


class ScreenConfig(BaseSettings):
    BACKGROUND: Image = Image(
        IMAGE='./assets/background.jpg',
        SIZE=Size(width=800, height=600)
    )
    LIFE_IMAGE: Image = Image(
        IMAGE='./assets/life.png',
        SIZE=Size(width=50, height=50)
    )
    DISPLAY_NAME: str = 'Мур ТВ'
    FONT_SIZE: int = 36
    FPS: int = 60


class GameConfig(BaseSettings):
    LIVES: int = 3


class BubbleHuntConfig(BaseSettings):
    SPRITES: SpritesConfig = SpritesConfig()
    SCREEN: ScreenConfig = ScreenConfig()
    GAME: GameConfig = GameConfig()


MUR_TV_SETTINGS = BubbleHuntConfig()
