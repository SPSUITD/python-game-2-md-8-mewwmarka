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

    MICE_CHANNEL: str = 'mur_tv/assets/mice.mp4'
    CHANNELS: Sequence[str] = (
        'mur_tv/assets/channel1.mp4',
        'mur_tv/assets/channel2.mp4',
        'mur_tv/assets/channel3.mp4',
        'mur_tv/assets/channel4.mp4',
        MICE_CHANNEL
    )
    FONT_SIZE: int = 36
    FPS: int = 60


class MurTvConfig(BaseSettings):
    SCREEN: ScreenConfig = ScreenConfig()


MUR_TV_SETTINGS = MurTvConfig()
