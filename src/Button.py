class Button():
    screen = None
    rect = None

    def __init__(self, color, leds):
        self.color = color
        self.leds = leds
        self.guiColor = color.value

    def toString(self):
        "Color: " + self.color.name + "\n" + self.leds.toString()

    def setDraw(self, screen, rect):
        self.screen = screen
        self.rect = rect

    def pressed(self):
        darken = [1/2, 1/2, 1/2]
        newColor = []
        for i in range(len(self.color.value)):
            newColor.append(round(self.color.value[i]*darken[i]))
        self.guiColor = newColor


    def resetGUIColor(self):
        self.guiColor = self.color.value

    def getGUIColor(self):
        return self.guiColor

    def addColor(self,list):
        list.append(self.color)