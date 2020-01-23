from enum import Enum

class Color(Enum):
    RED = [255, 0, 0]
    GREEN = [0, 255, 0]
    BLUE = [0, 0, 255]
    YELLOW = [255, 225, 25]
    WHITE = [255,255,255]
    PURPLE = [145,30,180]
    MAROON = [128,0,0]
    ORANGE = [245,130,48]
    BLACK = [0,0,0]
    LIGHT_GREY = [217, 207, 206]

    @staticmethod
    def toColor(text):
        switch = {
            "b": Color.BLUE,
            "blue": Color.BLUE,
            "r": Color.RED,
            "red": Color.RED,
            "g": Color.GREEN,
            "green": Color.GREEN,
            "y": Color.YELLOW,
            "yellow": Color.YELLOW,
            "w": Color.WHITE, 
            "white": Color.WHITE,
            "p": Color.PURPLE,
            "purple": Color.PURPLE,
            "m": Color.MAROON,
            "maroon": Color.MAROON,
            "o": Color.ORANGE,
            "orange": Color.ORANGE
        }
        return switch.get(text.lower(), False)