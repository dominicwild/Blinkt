class Button():
    def __init__(self, color, leds):
        self.color = color
        self.leds = leds

    def toString(self):
        "Color: " + self.color.name + "\n" + self.leds.toString()