from dataclasses import dataclass


@dataclass(frozen=True)
class Size:
    width: int
    height: int

    @property
    def to_tuple(self) -> [int, int]:
        return self.width, self.height


@dataclass(frozen=True)
class Speed:
    x: int
    y: int

    def __iter__(self):
        return iter((self.x, self.y))
