class ReactiveButton():
    isPressed = False

    def __init__(self, guiColor):
        self.guiColor = guiColor

    def pressed(self):
        self.guiColor = [i * 0.5 for i in self.color.value]  # Darken the colour
        self.isPressed = True

    def hovering(self):
        if (not self.isPressed):
            self.guiColor = self.hoverColor

    def resetGUIColor(self):
        self.guiColor = self.color.value

    def reset(self):
        self.resetGUIColor()
        self.isPressed = False
