from enum import Enum, auto, unique


@unique
class FrameType(Enum):
    SIZE = auto()
    CLOSE = auto()
