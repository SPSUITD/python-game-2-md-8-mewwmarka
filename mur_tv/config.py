from typing import Sequence

from pydantic_settings import BaseSettings

from bubble_hunt.value_objects import Size


class Image(BaseSettings):
    IMAGE: str
    SIZE: Size = Size(0, 0)


class ScreenConfig(BaseSettings):
    BACKGROUND: Image = Image(
        IMAGE='mur_tv/assets/background.jpg',
        SIZE=Size(width=800, height=600)
    )
    LIFE_IMAGE: Image = Image(
        IMAGE='mur_tv/assets/life.png',
        SIZE=Size(width=50, height=50)
    )
    IMAGES: Sequence[str] = (
        'mur_tv/assets/gagarin.mp4',
        'mur_tv/assets/kitten.mp4',
        'mur_tv/assets/cat_assassin.mp4',
    )
    MICE_IMAGE: str = 'mur_tv/assets/mice.png'
    DISPLAY_NAME: str = 'Мур ТВ'
    FONT_SIZE: int = 36
    FPS: int = 60


class GameConfig(BaseSettings):
    LIVES: int = 3


class MurTvConfig(BaseSettings):
    SCREEN: ScreenConfig = ScreenConfig()
    GAME: GameConfig = GameConfig()


MUR_TV_SETTINGS = MurTvConfig()
