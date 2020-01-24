from TextButton import TextButton


class BackButton(TextButton):

    def __init__(self, text, x, y, game):
        TextButton.__init__(self, text, x, y, game)

    def onClick(self):
        self.game.back()