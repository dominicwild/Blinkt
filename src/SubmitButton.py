from TextButton import TextButton


class SubmitButton(TextButton):

    def __init__(self, text, x, y, game):
        TextButton.__init__(self, text, x, y, game)

    def onClick(self):
        self.game.setSubmit(True)